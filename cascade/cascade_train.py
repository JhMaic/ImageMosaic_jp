import sys
import os
import cv2
import multiprocessing

POS_PATH = 'pos/'
NEG_PATH = 'neg/'

POS_DAT_NAME = 'pos.txt'
POS_VEC_NAME = 'pos.vec'
NEG_LIST_NAME = 'neg.txt'

CACHE_PATH = '.cache/'
CHECKPOINT_PATH = 'check_point/'

H, W = 30, 30

EPOCH = 12

# create neg text
print('creating negative image list ...')
neg_l = [NEG_PATH + n for n in os.listdir('neg')]
with open(NEG_LIST_NAME, 'w') as f:
    f.write('\n'.join(neg_l))

# create pos description data
print(f'total negative number is {len(neg_l)}')
print('creating positive image info list ...')
pos_data = []
for im in os.listdir('pos'):
    path = POS_PATH + im
    h, w, _ = cv2.imread(path).shape
    pos_data += [f'{path} 1 0 0 {w} {h}']

with open(POS_DAT_NAME, 'w') as f:
    f.write('\n'.join(pos_data))

# create samples
print(f'total positive number is {len(pos_data)}')
print('creating positive sample vectors ...')
os.system(f'opencv_createsamples -info {POS_DAT_NAME} -vec {POS_VEC_NAME} -num {len(pos_data)} -w {W} -h {H} -bgcolor 255 -bgthresh 5')
# os.system(f'opencv_createsamples -info {POS_DAT_NAME} -vec {POS_VEC_NAME} -num {len(pos_data)} -w {W} -h {H} -bg {NEG_LIST_NAME}')

# train cascade
print('start training ...')

os.system(f'mkdir {CACHE_PATH}')
os.system(f'mkdir {CHECKPOINT_PATH}')

train_command = 'opencv_traincascade ' + \
                '-data ' + CACHE_PATH + \
                ' -vec ' + POS_VEC_NAME + \
                ' -bg ' + NEG_LIST_NAME + \
                ' -numPos ' + str(int(len(pos_data) * 0.95)) + \
                ' -numNeg ' + str(len(neg_l)) + \
                ' -stageType BOOST' + \
                ' -featureType LBP' + \
                ' -w ' + str(W) + \
                ' -h ' + str(H) + \
                ' -bt GAB' + \
                ' -minHitRate 0.999' + \
                ' -maxFalseAlarmRate 0.05' + \
                ' -maxDepth 1' + \
                ' -precalcValBufSize 6000' + \
                ' -precalcIdBufSize 6000' + \
                ' -numThreads ' + str(multiprocessing.cpu_count())

for i in range(EPOCH):
    command = train_command + f' -numStages {i+1}'
    os.system(command)
    os.system(f'cp {CACHE_PATH}/cascade.xml {CHECKPOINT_PATH}/stage{i+1}.xml')


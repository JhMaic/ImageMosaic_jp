import time

import cv2

from mosaic import ImageMosaic

if __name__ == '__main__':
    start = time.time()
    im = ImageMosaic()
    im.mosaic('imgs')
    end = time.time()

    print(end - start)
    # image = cv2.imread('imgs/IMG_0417.jpg')
    # net = cv2.dnn.readNet('yolov4-tiny.cfg', 'yolov4-tiny.weights')
    # model = cv2.dnn_DetectionModel(net)
    # model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)
    #

    # detect_result = model.detect(image, confThreshold=0.1, nmsThreshold=0.1)
    # print(detect_result)
    #
    # for object_class, [x, y, w, h] in zip(detect_result[0], detect_result[2]):
    #     if object_class == 0:
    #         face = image[y: y + h, x: x + w]
    #         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #
    #         cv2.imshow('img', image)
    #         cv2.waitKey()

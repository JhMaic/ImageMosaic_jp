im_path = 'x1/1/plate0002.jpg'

from PIL import Image, ImageChops
import os

# remove white surrounding
def trim(im):
    bg = Image.new(im.mode, im.size, 'white')
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 1.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

# im = Image.open(im_path)
# im = trim(im)
# im.save(f'trim_image/{}')

im_list = os.listdir('x1')
n_fail = 0
for im_path in im_list:
    try:
        im = Image.open(f'x1/{im_path}')
        im = trim(im)
        im.save(f'trim_image/{im_path}')
    except Exception as e:
        n_fail += 1

print(f'totally processed: {len(im_list)}\n failed: {n_fail}')
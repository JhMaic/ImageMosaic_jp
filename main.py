import time

import cv2

from mosaic import ImageMosaic

if __name__ == '__main__':
    start = time.time()
    im = ImageMosaic(text_recognize=False)
    im.mosaic('imgs')
    end = time.time()

    print(end - start)
import time

import cv2
import numpy as np
from mosaic import ImageMosaic

if __name__ == '__main__':
    start = time.time()
    im = ImageMosaic(text_recognize=False, easy_ocr=False)
    im.mosaic('imgs')
    end = time.time()


    print(end - start)


    # from craft_text_detector import Craft
    #
    #
    # # set image path and export folder directory
    # image = 'imgs/4241b3576a990939df4aa6afd9cbdbdb.jpg'  # can be filepath, PIL image or numpy array
    # output_dir = 'outputs/'
    #
    # # create a craft instance
    # craft = Craft(output_dir=output_dir, cuda=False, text_threshold=0.1)
    #
    # # apply craft text detection and export detected regions to output directory
    # prediction_result = craft.detect_text(image)

import cv2

if __name__ == '__main__':
    # im = ImageMosaic()
    # im.mosaic('imgs')
    image = cv2.imread('imgs\\frame0.jpg')
    net = cv2.dnn.readNet('yolov4-tiny.cfg', 'yolov4-tiny.weights')
    model = cv2.dnn_DetectionModel(net)
    model.setInputParams(scale=1 / 255, size=(416, 416), swapRB=True)

    # 物体検出
    detect_result = model.detect(image, confThreshold=0.6, nmsThreshold=0.4)
    print(detect_result)

    for object_class, [x, y, w, h] in zip(detect_result[0], detect_result[2]):
        if object_class == 0:
            face = image[y: y + h, x: x + w]
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow('img', image)
            cv2.waitKey()

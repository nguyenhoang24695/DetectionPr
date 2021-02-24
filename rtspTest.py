import cv2 as cv

vcap = cv.VideoCapture("rtsp://hoangnv:11111111A@117.6.22.186:554/cam/realmonitor?channel=1&subtype=0")

while 1:
    ret, frame = vcap.read()
    if ret:
        height, width, layers = frame.shape
        new_h = height // 2
        new_w = width // 2
        resize = cv.resize(frame, (new_w, new_h))
        cv.imshow('VIDEO', resize)
        cv.waitKey(1)

import cv2
import numpy as np


def main():
    
    windowName = "Preview"
    cv2.namedWindow(windowName)
    cap = cv2.VideoCapture(0)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False


    while ret:
    
        ret, frame = cap.read()
        
        
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY	)
        blur = cv2.blur(frame, (15, 15))
       

        circles = cv2.HoughCircles(grey, method=cv2.HOUGH_GRADIENT,
                                   dp=1, minDist=20, param1=90, param2=5,
                                   minRadius=1, maxRadius=3)

        
        cv2.imshow(windowName,circles)

        if cv2.waitKey(1) == 27: # exit on ESC
            break

    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()

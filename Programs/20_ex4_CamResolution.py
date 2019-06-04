import cv2

def main():

    windowName = "Live video feed"
    cv2.namedWindow(windowName)
    
    windowName1 = "Live video feed 1"
    cv2.namedWindow(windowName1)

    Regular = "video feed"
    cv2.namedWindow(Regular)
    
    Regular1 = "video feed"
    cv2.namedWindow(Regular1)

    cap = cv2.VideoCapture(0)
    cap1 =cv2.VideoCapture(1)
	
    #video of lappy webcam.
    if cap.isOpened():
        ret,frame = cap.read()
    else:
        ret = False

    print("Width = " + str(cap.get(3)))
    print("Height = " + str(cap.get(4)))

    cap.set(3, 3000)
    cap.set(4, 3000)

    print("Width = " + str(cap.get(3)))
    print("Height = " + str(cap.get(4)))

    while ret:
        ret,frame= cap.read()
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
        cv2.imshow (Regular, frame)   
        cv2.imshow(windowName,output)

        if cv2.waitKey(1)==27:
            break
    cv2.destroyWindow(windowName)
    cv2.destroyWindow(Regular)

    cap.release()

	# video of external cam
    if cap1.isOpened():
        ret1,frame1 = cap1.read()
    else:
        ret1 = False
    print("\n")
    print("Width1 = " + str(cap1.get(3)))
    print("Height1 = " + str(cap1.get(4)))

    cap1.set(3, 100)
    cap1.set(4, 100)

    print("Width1 = " + str(cap1.get(3)))
    print("Height1 = " + str(cap1.get(4)))

    while ret1:
        ret1,frame1= cap1.read()
        output1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)    
        cv2.imshow ('Regular1', frame1)
        cv2.imshow(windowName1,output1)

        if cv2.waitKey(1)==27:
            break
    cv2.destroyWindow(windowName1)
    cv2.destroyWindow(Regular1)
    
    cap1.release()

if __name__== "__main__":
    main() 

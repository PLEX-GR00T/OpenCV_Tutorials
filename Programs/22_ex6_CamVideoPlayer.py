import cv2
def main():
    	
    #-------------------------------------video of internal webcam-----------------------------------
	
    windowName = "VIDEO PLAYER 0 RGB."
    cv2.namedWindow(windowName)
    filename_reg = "/home/g_r00t/PRIYANK/output/intr_BGR_Form.avi"
    cap1 = cv2.VideoCapture(filename_reg)
	    
    Regular = "VIDEO PLAYER 1 Regular"
    cv2.namedWindow(Regular)
    filename_nreg = "/home/g_r00t/PRIYANK/output/intr_RGB_Form.avi"
    cap = cv2.VideoCapture(filename_nreg)
    
    while (cap1.isOpened()):
    
        ret1,frame1= cap1.read()
        print(ret1)
        
        if ret1:
            cv2.imshow (Regular, frame1)
            if cv2.waitKey(17)==27:
                break
        else:
            break
    		
    cv2.destroyWindow(Regular)
    cap1.release()	    	

    while (cap.isOpened()):
        
        ret,frame= cap.read()
        print(ret)
        
        if ret:
            output=cv2. cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.imshow (Regular, output)
            if cv2.waitKey(33)==27:
                break
        else:
            break
    		
    cv2.destroyWindow(Regular)
    cap.release()
if __name__== "__main__":
    main() 
 	

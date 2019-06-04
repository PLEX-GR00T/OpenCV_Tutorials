import cv2
import numpy as np
def main():
 
    cap = cv2.VideoCapture(0)
    
	#----------------------------------video of lappy webcam.--------------------------------------
	
    if cap.isOpened():
        ret,frame = cap.read()
    else:
        ret = False

    while ret:
        ret,frame= cap.read()
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        #---BLUE COLOR DETECTION.----
        #low = np.array([50,50,50])
        #high = np.array([140,255,255])
        
        #---GREEN COLOR DETECTION------
        low = np.array([50,50,50])
        high = np.array([80,255,255])
        
        #-----RED COLOR DETECTION-------
        #low = np.array([140,50,10])
        #high = np.array([180,255,255])
        
        image_mask = cv2.inRange(hsv,low,high)
        output = cv2.bitwise_and(frame, frame,mask = image_mask)
        
        cv2.imshow("BitWise AND image", output)
        cv2.imshow("Image Mask", image_mask)
        print(hsv)
        cv2.imshow("Regular",frame)
        cv2.imshow("HSV WINDOW", hsv)    
        if cv2.waitKey(1)==27:
            break
            
    cv2.destroyAllWindows()
    cap.release()

if __name__=="__main__":
	main()

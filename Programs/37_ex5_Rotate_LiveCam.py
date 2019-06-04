import cv2
import time

def main():
	windowName='Live cam rotation.'
	cv2.namedWindow(windowName)
	cap=cv2.VideoCapture(0)
	
	if cap.isOpened():
		ret,frame=cap.read()
	else:
		ret=False
		
	rows,columns,channels=frame.shape
	
	angle=0
	scale=0
	
	while True:
		ret,frame= cap.read()
		
		if angle==360:
			angle=0
		
		if scale<1:
			scale=scale+0.1
				
		if scale>1:
			scale=0.1
			
		print(scale)		
		R1 = cv2.getRotationMatrix2D((columns/2,rows/2),angle,scale)
		#print(R1)
		output=cv2.warpAffine(frame,R1,(columns,rows))
		
		cv2.imshow(windowName,output)
		angle = angle+1
		time.sleep(0.01)
		
		if cv2.waitKey(1)==27:
			break
			
	cv2.destroyAllWindows()
	cap.release()		

if __name__== "__main__":
    main() 

import cv2
import numpy as np

def emptyfun():
	pass
	
def main():

	img1 = np.zeros((512,512,3),np.uint8)
	WindowName = 'OpenCV BRG Color Palette'
	cv2.namedWindow(WindowName)
	
	cv2.createTrackbar('B', WindowName, 0,255, emptyfun)
	cv2.createTrackbar('G', WindowName, 0,255, emptyfun)
	cv2.createTrackbar('R', WindowName, 0,255, emptyfun)
	
	while(True):
	
		cv2.line(img1,(0,512),(512,0),(123,241.0),2)
		cv2.rectangle(img1,(50,100),(250,20),(0,0,255),2)
		cv2.circle(img1,(256,256),80,(204,0,2),-1)
		cv2.ellipse(img1,(400,400),(80,20),0,0,360,(0,255,0),2)
		
		points = np.array([[100,100],[100,200],[200,200],[200,100],[150,150]],np.int32)
		points = points.reshape((-1,1,2)) #(i dont know how it works.)
		cv2.polylines(img1,[points],True,(127,127,127))
	
		text1 = 'Priyank'
		cv2.putText(img1, text1, (350,408), cv2.FONT_HERSHEY_SIMPLEX,1,(20,60,255))
	
		cv2.imshow(WindowName,img1)
		
		if cv2.waitKey(1)==27:
			break
		
		Blue = cv2.getTrackbarPos('B', WindowName)
		Green = cv2.getTrackbarPos('G', WindowName)
		Red = cv2.getTrackbarPos('R', WindowName)
		
		img1[:] = [Blue,Green,Red]
		print(Blue,Green,Red)	
		
	cv2.destroyAllWindows()
	
if __name__=="__main__":
	main()

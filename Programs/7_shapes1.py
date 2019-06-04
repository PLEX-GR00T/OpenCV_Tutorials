import cv2
import numpy as np

def main():
	img1=np.zeros((512,512,3),np.uint8)
	
	cv2.line(img1,(0,512),(512,0),(123,241.0),2)
	cv2.rectangle(img1,(50,100),(250,20),(0,0,255),2)
	cv2.circle(img1,(256,256),80,(204,0,2),-1)
	cv2.ellipse(img1,(400,400),(80,20),0,0,360,(0,255,0),2)
	
	points = np.array([[100,100],[100,200],[200,200],[200,100],[150,150]],np.int32)
	points = points.reshape((-1,1,2)) #(i dont know how it works.)
	print(points)
	cv2.polylines(img1,[points],True,(127,127,127), lineType = cv2.LINE_8)
	
	text1 = 'Priyank'
	cv2.putText(img1, text1, (350,408), cv2.FONT_HERSHEY_SIMPLEX,1,(20,60,255))
	
	cv2.imshow('WINDOW',img1)
	cv2.waitKey(0)
	cv2.destroyWindow('WINDOW')
	
if __name__=="__main__":
	main()

import cv2
import numpy as np

windowName = 'Drawing Demo'
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow(windowName)
i = 0

def draw_circle(event, x, y,flags,param):
	global i
	if event == cv2.EVENT_RBUTTONDOWN:
		cv2.circle(img, (x,y), 10, (255,0,0),-1)
	
	if event == cv2.EVENT_LBUTTONUP:
		cv2.circle(img, (x,y), 40, (0,i,0), -1)
		if i+10 <= 255:
			i=i+10
			if i==250:
				print("you hav reached the final position.")
				i = 0
				print(i)
		print(i)	
		
	if event == cv2.EVENT_MBUTTONDBLCLK:
		cv2.circle(img, (x,y), 20, (0,0,255),-1)
					
	
cv2.setMouseCallback(windowName, draw_circle)

def main():
	while(True):
		cv2.imshow(windowName,img)
		if cv2.waitKey(1)==27:
			break
	cv2.destroyAllWindows()
	
if __name__=="__main__":
	main()

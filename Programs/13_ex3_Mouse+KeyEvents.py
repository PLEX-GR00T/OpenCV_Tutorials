import cv2
import numpy as np

windowName = 'Drawing demo'
img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow(windowName)

drawing = False

mode = False
(ix, iy) = (-1,-1)
def draw_Shape(event,x,y,flags,param):
	global ix,iy, drawing, mode
	
	if event == cv2.EVENT_LBUTTONDOWN:
		drawing = True
		(ix, iy) = x,y
		
	elif event == cv2.EVENT_MOUSEMOVE:
		if drawing == True:
			if mode == True:
				cv2.rectangle(img, (ix,iy), (x,y), (0,255,0),-1)
			else:
				cv2.circle(img, (x,y),30, (0,0,255),-1)		
	
	elif event == cv2.EVENT_LBUTTONUP:
		drawing = False
		if mode == True:
			cv2.rectangle(img, (ix,iy), (x,y), (0,255,0),-1)
		else:
			cv2.circle(img, (x,y),30, (0,0,255),-1)

cv2.setMouseCallback(windowName, draw_Shape)	

def main():	
	global mode
	
	while(True):
		cv2.imshow(windowName,img)
		
		k = cv2.waitKey(1)
		if k == ord('m') or k == ord('M'):
			mode = not mode
		elif k == 27:
			break
			
	cv2.destroyAllWindows()	
			
if __name__=="__main__":
	main()				 

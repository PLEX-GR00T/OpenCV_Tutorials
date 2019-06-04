import cv2
import numpy as np

windowName = 'Drawing Demo'
img = np.zeros((1000,1000,3), np.uint8)
cv2.namedWindow(windowName)
b = 0
g = 0
r = 0

def draw_circle(event, x, y,flags,param):
	global b
	global g
	global r
	#if event == cv2.EVENT_LBUTTONDBLCLK:
	if event == cv2.EVENT_MOUSEMOVE:
		cv2.circle(img, (x,y), 40, (b,g,r), -1)
		if b < 255:
			if g < 255:
				if (r < 255):
					r = r + 15
				else:
					r = 0
					g = g + 15
			else:
				g = 0
				b = b + 15
		else:
			b = 0
		print("BGR: ", b, g, r)				
	
cv2.setMouseCallback(windowName, draw_circle)

def main():
	while(True):
		cv2.imshow(windowName,img)
		if cv2.waitKey(1)==27:
			break
	cv2.destroyAllWindows()
	
if __name__=="__main__":
	main()

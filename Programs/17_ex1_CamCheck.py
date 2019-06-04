import cv2
import matplotlib.pyplot as plt

def main():

	
	cap1 = cv2.VideoCapture(1)
	if cap1.isOpened():
		ret1, frame1 = cap1.read()
		print('this is cap1')
		print(ret1)
		print(frame1)
	else:
		ret1 = False
		
		
	cap = cv2.VideoCapture(0)
	if cap.isOpened():
		ret, frame= cap.read()
		print('this is cap0')
		print(ret)
		print(frame)
	else:
		ret = False
		
	img1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
	img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	
	plt.imshow(img1)
	plt.title('webcame1')
	plt.xticks([])
	plt.yticks([])
	plt.show()
	
	plt.imshow(img)
	plt.title('webcame')
	plt.xticks([])
	plt.yticks([])
	plt.show()	
	
	cap1.release()
	cap.release()
		
if __name__=="__main__":
	main()	


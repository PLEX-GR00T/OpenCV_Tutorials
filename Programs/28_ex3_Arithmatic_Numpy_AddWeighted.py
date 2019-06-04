import cv2
import numpy as np
import time



def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath1 = path + "lena_color_512.tif"
	imgpath2 = path + "woman_blonde.tif"
	
	img1=cv2.imread(imgpath1,1)
	img2=cv2.imread(imgpath2,1)

	flag=True
		
	while flag:
		for i in np.linspace (0,1,40):
			alpha = i
			beta =1-alpha
			gamma = 0
			output = cv2.addWeighted(img1,alpha,img2,beta,gamma)
			cv2.imshow('Transition',output)
			time.sleep(0.1)
			
			if cv2.waitKey(1) == 27:
				flag= False
				break
		cv2.destroyAllWindows()
		
		if beta==0:
			for i in np.linspace (0,1,40):
				alpha = i
				beta =1-alpha
				gamma = 0
								
				output = cv2.addWeighted(img2,alpha,img1,beta,gamma)
				cv2.imshow('Transition',output)
				time.sleep(0.1)
					
				if cv2.waitKey(1) == 27:
					flag= False
					break				
			
	cv2.destroyAllWindows()

if __name__=="__main__":
	main()	
	


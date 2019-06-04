import cv2
import matplotlib.pyplot as plt
import numpy as np
import random

def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath= path+"4.2.01.tiff"
	
	img = cv2.imread(imgpath,1)
	img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	
	rows,columns,channels =img.shape
	p=0.05
	
	output=np.zeros(img.shape,np.uint8)
	
	for i in range(rows):
		for j in range(columns):
			r=random.random()
			if r < p/2:
				output[i][j]=[0,0,0] #pepper sprinkle
			elif r < p:
				output[i][j]=[255,255,255]
			else:
				output[i][j]=img[i][j]
	plt.imshow(output) 
	plt.title("image with the salt")
	plt.show()
if __name__=="__main__":
	main()

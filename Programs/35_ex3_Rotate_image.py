import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath1 = path + "4.2.01.tiff"	
	img = cv2.imread(imgpath1,1)
	img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	
	rows,columns,channels = img.shape
	
	R1 = cv2.getRotationMatrix2D((columns/5,rows/5),0,0.3)
	R2 = cv2.getRotationMatrix2D((columns/2,rows/2),10,0.5)
	R3 = cv2.getRotationMatrix2D((columns/7,rows/2),20,0.5)
	R4 = cv2.getRotationMatrix2D((columns/2,rows/2),30,0.5)
	
	R5 = cv2.getRotationMatrix2D((columns/2,rows/6),45,0.7)
	R6 = cv2.getRotationMatrix2D((columns/2,rows/2),90,0.7)
	R7 = cv2.getRotationMatrix2D((columns/4,rows/2),180,0.7)
	R8 = cv2.getRotationMatrix2D((columns/2,rows/9),-45,0.7)
	
	print(R1,R2,R3)
	
	output1=cv2.warpAffine(img1,R1,(columns,rows))
	output2=cv2.warpAffine(img1,R2,(rows,columns))
	output3=cv2.warpAffine(img1,R3,(columns,rows))
	output4=cv2.warpAffine(img1,R4,(columns,rows))
	
	output5=cv2.warpAffine(img1,R5,(columns,rows))
	output6=cv2.warpAffine(img1,R6,(columns,rows))
	output7=cv2.warpAffine(img1,R7,(columns,rows))
	output8=cv2.warpAffine(img1,R8,(columns,rows))
	
	output = [output1,output2,output3,output4,output5,output6,output7,output8]
	title = ['img1','img2','img3','img4','img5','img6','img7','img8']
	
	for i in range (8):	
		plt.subplot(2,4,i+1)	
		plt.imshow(output[i])
		plt.title(title[i])
		#plt.axis("off")
	
	plt.show()
		
if __name__=="__main__":
	main()	


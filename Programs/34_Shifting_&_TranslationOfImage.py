import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath1 = path + "4.2.01.tiff"	
	img = cv2.imread(imgpath1,1)
	img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	
	rows,columns,channels = img.shape
	
	T1=np.float32([[2,0,0],[0,1,100]])
	T2=np.float32([[1,0,-50],[0,1,-50]])
	T3=np.float32([[1,0,-50],[0,1,50]])
	T4=np.float32([[0,1,0],[1,0,50]])

	T5=np.float32([[1,0,50],[0,2,-50]])
	T6=np.float32([[2,0,-50],[0,2,-50]])
	T7=np.float32([[2,0,-50],[0,2,50]])
	T8=np.float32([[2,0,50],[0,2,50]])
	
	print(T1,T2,T3)
	
	output1=cv2.warpAffine(img1,T1,(columns,rows))
	output2=cv2.warpAffine(img1,T2,(rows,columns))
	output3=cv2.warpAffine(img1,T3,(columns,rows))
	output4=cv2.warpAffine(img1,T4,(columns,rows))
	
	output5=cv2.warpAffine(img1,T5,(columns,rows))
	output6=cv2.warpAffine(img1,T6,(columns,rows))
	output7=cv2.warpAffine(img1,T7,(columns,rows))
	output8=cv2.warpAffine(img1,T8,(columns,rows))
	
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


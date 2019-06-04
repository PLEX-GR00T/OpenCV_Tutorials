import cv2
import matplotlib.pyplot as plt

def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath1 = path + "house.tiff"
	imgpath2 = path + "lena_color_512.tif"
	
	img10 = cv2.imread(imgpath1,1)
	img20 = cv2.imread(imgpath2,1)
	
	img1 = cv2.cvtColor(img10,cv2.COLOR_BGR2RGB)
	img2 = cv2.cvtColor(img20,cv2.COLOR_BGR2RGB)

	img3 = cv2.bitwise_not(img1)
	img4 = cv2.bitwise_and(img1,img2)
	img5 = cv2.bitwise_or(img1,img2)
	img6 = cv2.bitwise_xor(img1,img2)
	
	img7 = abs(255-img1)
	img8 = img1-img2
	img9 = img1+img2
	img11 = img1*img2
	
	img_titles = ["original-1","original-2","Image1","Image2","NOT",'AND','OR','XOR','NGATIVE','SUB','ADD','MUL']	
	show_images = [img10,img20,img1,img2,img3,img4,img5,img6,img7,img8,img9,img11]
	
	for i in range (12):
		plt.subplot(3,4,i+1)	
		plt.imshow(show_images[i])
		plt.title(img_titles[i])
		plt.xticks([])
		plt.yticks([])  # to removee the scales from the graph
		
	plt.show()
		
if __name__=="__main__":
	main()	


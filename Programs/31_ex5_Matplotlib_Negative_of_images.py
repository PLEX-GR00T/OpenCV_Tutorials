import cv2
import matplotlib.pyplot as plt

def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath1 = path + "house.tiff"

	
	img = cv2.imread(imgpath1,1)
	img1 = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	img2 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	img3 = abs(255-img1)
	img4 = abs(255-img2)
	
	plt.subplot(2,2,1)	
	plt.imshow(img1)
	plt.title("Original_color")
	plt.axis("off")
	
	plt.subplot(2,2,2)	
	plt.imshow(img2,cmap='gray')
	plt.title("Original_gray")
	plt.axis("off")
	
	plt.subplot(2,2,3)	
	plt.imshow(img3)
	plt.title("Negative_color")
	plt.axis("off")
	
	plt.subplot(2,2,4)	
	plt.imshow(img4,cmap='gray')
	plt.title("Negative_Gray")
	plt.axis("off")
	
	plt.show()
		
if __name__=="__main__":
	main()	


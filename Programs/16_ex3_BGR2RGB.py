import cv2
import matplotlib.pyplot as plt

def main():
	imgpath="/home/g_r00t/PRIYANK/ex_images/lena_color_512.tif"
		
	img = cv2.imread(imgpath,1)
	img4 =cv2.imread(imgpath,0)
	
	img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	
	plt.imshow(img)
	plt.title('Default colormap')
	plt.xticks([100])
	plt.yticks([500])  # to removee the scales from the graph
	plt.show()

	plt.imshow(img4,cmap='hsv')	#conclusion: to convert the gray image to multi color use plt & to covert the regular image to diff color use cv2.cvtColor().
	plt.title('RGB form')
	plt.show()
	
	plt.imshow(img2)
	plt.title('COLOR_BGR2HSV')
	plt.show()
	
	plt.imshow(img3)
	plt.title('BGR2GRAY')
	plt.xticks([])
	plt.yticks([])  # to removee the scales from the graph
	plt.show()
	
if __name__=="__main__":
	main()	
	


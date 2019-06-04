import cv2
import matplotlib.pyplot as plt

def main():
	imgpath="/home/g_r00t/PRIYANK/ex_images/lena_color_512.tif"
	img = cv2.imread(imgpath,0)
	
	plt.imshow(img, cmap='gray')		#this wrong method showa all the possible cmap colors.
	plt.title('Plasma colormap')
	plt.show()
	
	plt.imshow(img)
	plt.title('Default colormap')
	plt.xticks([])
	plt.yticks([])  # to removee the scales from the graph
	plt.show()

	plt.imshow(img, cmap='plasma')
	plt.title('Plasma colormap')
	plt.show()
	
	plt.imshow(img, cmap='Spectral')
	plt.title('sectral colormap')
	plt.show()
	
	plt.imshow(img, cmap=	'PiYG_r')
	plt.title('Piygr colormap')
	plt.xticks([])
	plt.yticks([])  # to removee the scales from the graph
	plt.show()
	
if __name__=="__main__":
	main()	
	
	

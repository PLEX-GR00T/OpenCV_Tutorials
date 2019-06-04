import cv2
import matplotlib.pyplot as plt

def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath1 = path + "lena_color_256.tif"
	imgpath2 = path + "woman_blonde.tif"

	img1=cv2.imread(imgpath1,1)
	img2=cv2.imread(imgpath2,0)
		
	plt.subplot(2,2,1)	
	plt.imshow(img1)
	plt.title('Default colormap')
	plt.xticks([])
	plt.yticks([])  # to removee the scales from the graph

	plt.subplot(2,2,2)
	plt.imshow(img1, cmap='plasma')
	plt.title('Plasma colormap')
	
	plt.subplot(2,2,3)
	plt.imshow(img2, cmap='Spectral')
	plt.title('sectral colormap')
	
	plt.subplot(2,2,4)
	plt.imshow(img2, cmap='PiYG_r')
	plt.title('Piygr colormap')
	plt.xticks([])
	plt.yticks([])  # to removee the scales from the graph
	
	plt.show()
	
if __name__=="__main__":
	main()	
	


import cv2
import matplotlib.pyplot as plt

def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath1 = path + "woman_blonde.tif"
	imgpath2 = path + "lena_color_512.tif"
	imgpath3 = path + "4.2.03.tiff"
	imgpath4 = path + "4.2.01.tiff"
	
	img1=cv2.imread(imgpath1,0)
	img2=cv2.imread(imgpath2,0)
	img3=cv2.imread(imgpath3,0)
	img4=cv2.imread(imgpath4,0)
		
	img_titles = ["Original","Image1","Image2","Image3","Image"]	
	show_images = [img1,img2,img3,img4]
	cmaps = ['gray','Spectral','PiYG_r','plasma']
	
	for i in range (4):
		plt.subplot(2,2,i+1)	
		plt.imshow(show_images[i],cmaps[i])
		plt.title(img_titles[i])
		plt.xticks([])
		plt.yticks([])  # to removee the scales from the graph
		
	plt.show()
	
if __name__=="__main__":
	main()	
	


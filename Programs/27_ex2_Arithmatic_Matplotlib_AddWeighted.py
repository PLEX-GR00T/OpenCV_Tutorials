import cv2
import matplotlib.pyplot as plt

def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath1 = path + "lena_color_512.tif"
	imgpath2 = path + "woman_blonde.tif"
	
	img1=cv2.imread(imgpath1,1)
	img2=cv2.imread(imgpath2,1)
	
	img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	img2=cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
	
	alpha=0.5
	beta=0.5
	gamma=0
	
	output=cv2.addWeighted(img1,alpha,img2,beta,gamma)
	
	img_titles = ["Image1","Image2","Wighted Image"]	
	show_images = [img1,img2,output]
	
	for i in range (3):
		plt.subplot(1,3,i+1)	
		plt.imshow(show_images[i])
		plt.title(img_titles[i])
		plt.xticks([])
		plt.yticks([])  # to removee the scales from the graph
		
	plt.show()
	
if __name__=="__main__":
	main()	
	


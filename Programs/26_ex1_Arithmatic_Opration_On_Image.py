import cv2
import matplotlib.pyplot as plt

def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath1 = path + "lena_color_512.tif"
	imgpath2 = path + "woman_blonde.tif"
	imgpath3 = path + "4.2.03.tiff"
	imgpath4 = path + "house.tiff"
	
	img1=cv2.imread(imgpath1,1)
	img2=cv2.imread(imgpath2,1)
	img3=cv2.imread(imgpath3,1)
	img4=cv2.imread(imgpath4,1)
	
	img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	img2=cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
	img3=cv2.cvtColor(img3, cv2.COLOR_BGR2RGB)
	img4=cv2.cvtColor(img4, cv2.COLOR_BGR2RGB)
	
	add = img1+img2
	sub = img3-img4
	mult = img2*img4
	div = img4/img1

	add1 = img1+60
	sub1 = img2-100
	mult1 = img3*1+sub1
	div1 = img4/500
			
	img_titles = ["Image1","Image2","Image3","Image4",'Add','Sub','Mul','Div','Add1','Sub1','Mul1','Div1']	
	#show_images = [img1,img2,img3,img4]
	show_images = [img1,img2,img3,img4,add,sub,mult,div,add1,sub1,mult1,div1]
	#cmaps = ['plasma','Spectral','PiYG_r','gray']
	
	for i in range (12):
		plt.subplot(3,4,i+1)	
		plt.imshow(show_images[i])
		plt.title(img_titles[i])
		plt.xticks([])
		plt.yticks([])  # to removee the scales from the graph
		
	plt.show()
	
if __name__=="__main__":
	main()	
	


import cv2
import matplotlib.pyplot as plt

def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath1 = path + "4.2.01.tiff"

	
	img1=cv2.imread(imgpath1,1)
	img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
	
	r,g,b=cv2.split(img1)

	imgpath2 = path + "4.2.01.tiff"
	img3=cv2.imread(imgpath2,0)
	img2 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
	r1,g1,b1=cv2.split(img2)
	
		
	img_titles = ["Red","Green","Blue","gray_r","gray_g","gray_b","Plasma_r","Plasma_g","Plasma_b"]	
	cmaps = ['Reds','Greens','Blues','gray','gray','gray','hsv','hsv','hsv']
	show_image=[r,g,b,r,g,b,r,g,b]
	
#-----matplotlib na original color/gray/hsv-----------------------------------
	plt.subplot(5,3,13)	
	plt.imshow(cv2.merge((r,g,b)))
	plt.title("Original")
	plt.xticks([])
	plt.yticks([])  # to removee the scales from the graph
	
	plt.subplot(5,3,14)	
	plt.imshow(img3,cmap='gray')
	plt.title("Original_gray")
	plt.xticks([])
	plt.yticks([])  # to removee the scales from the graph
	
	plt.subplot(5,3,15)	
	plt.imshow(img3,cmap='hsv')
	plt.title("Original_hsv")
	plt.xticks([])
	plt.yticks([])  # to removee the scales from the graph
	
#------matplotlib na original na 3 splits = r / g /  b------------------------
	plt.subplot(5,3,10)	
	plt.imshow(r)
	plt.title("r")
	plt.xticks([])
	plt.yticks([])  # to removee the scales from the graph
	
	plt.subplot(5,3,11)	
	plt.imshow(g)
	plt.title("g")
	plt.xticks([])
	plt.yticks([])  # to removee the scales from the graph
	
	plt.subplot(5,3,12)	
	plt.imshow(b)
	plt.title("b")
	plt.xticks([])
	plt.yticks([])  # to removee the scales from the graph

#--------r/g/b splits with different cmap color theme.---------------------------	
	for i in range (9):
		plt.subplot(5,3,i+1)	
		plt.imshow(show_image[i],cmaps[i])
		plt.title(img_titles[i])
		plt.xticks([])
		plt.yticks([])  # to removee the scales from the graph
		
	plt.show()
	
if __name__=="__main__":
	main()	
	


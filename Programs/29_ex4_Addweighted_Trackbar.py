import cv2

def emptyFunction():
	pass

def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath1 = path + "lena_color_512.tif"
	imgpath2 = path + "woman_blonde.tif"
	
	img1=cv2.imread(imgpath1,1)
	img2=cv2.imread(imgpath2,1)
	
	#img1=cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	#img2=cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
	
	output=cv2.addWeighted(img1,0.5,img2,0.5,0)
	
	windowName= "Trasition Demo"
	cv2.namedWindow(windowName)
	
	cv2.createTrackbar('Alpha',windowName,0,100,emptyFunction)
	flag = True
	while(flag):
		cv2.imshow(windowName,output)
		if cv2.waitKey(1)==27:
			flag= False
			break
			
		alpha = cv2.getTrackbarPos('Alpha',windowName)/100
		beta =1-alpha	
		output= cv2.addWeighted(img1,alpha,img2,beta,0)
		
		print(alpha,beta)
	cv2.destroyWindow('Transion Demo')
	
if __name__=="__main__":
	main()
	
	
	
if __name__=="__main__":
	main()	
	


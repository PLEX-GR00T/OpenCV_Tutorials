import cv2

def main():
	imgpath="/home/g_r00t/PRIYANK/ex_images/lena_color_512.tif"
	img = cv2.imread(imgpath, 0)  #by default value is 1. (0 =for gray scale image, -1 = show colored alpha transperancy image) 
	
	cv2.namedWindow('Lena',cv2.WINDOW_AUTOSIZE)
	cv2.imshow('Lena',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows('Lena')

if __name__=="__main__":
	main()	



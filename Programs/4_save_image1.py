import cv2

def main():
	imgpath="/home/g_r00t/PRIYANK/ex_images/lena_color_256.tif"
	img = cv2.imread(imgpath, 0) 
	img1 = cv2.imread(imgpath)
	
	outpath="/home/g_r00t/PRIYANK/output/lena_color_256.jpeg"
	
	cv2.namedWindow('Lena',cv2.WINDOW_AUTOSIZE)
	cv2.imshow('Lena',img)
	cv2.imwrite(outpath,img1)
	cv2.waitKey(0)
	cv2.destroyAllWindows('Lena')

if __name__=="__main__":
	main()	



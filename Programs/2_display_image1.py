import cv2

def main():
	imgpath="/home/g_r00t/PRIYANK/ex_images/lena_color_512.tif"
	img = cv2.imread(imgpath)
	
	cv2.imshow('Lena',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__=="__main__":
	main()	



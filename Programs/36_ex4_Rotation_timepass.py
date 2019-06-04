import cv2
import time

def main():
	path="/home/g_r00t/PRIYANK/ex_images/"
	imgpath1 = path + "4.2.01.tiff"	
	img = cv2.imread(imgpath1)
	rows,columns,channels = img.shape
	
	angle = 0
	while True:
		if angle == 360:
			angle = 0
		
		R1 = cv2.getRotationMatrix2D((columns/2,rows/2),angle,1)
		print(R1)
		output=cv2.warpAffine(img,R1,(columns,rows))
		
		cv2.imshow('Rotation Image',output)
		angle = angle+1
		time.sleep(0.01)
		
		if cv2.waitKey(1)==27:
			break
			
	cv2.destroyAllWindow()
	
if __name__=="__main__":
	main()	


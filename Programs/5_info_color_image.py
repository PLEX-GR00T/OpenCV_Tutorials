import cv2

def main():
	imgpath="/home/g_r00t/PRIYANK/ex_images/lena_color_256.tif"
	img = cv2.imread(imgpath)
		### COLORED IMAGE ###
	print(type(img))	#<class 'numpy.ndarray'>
	print(img.dtype)	#uint8  (8 bits = (00000000 to 11111111) = (0x00 to 0xFF) = (0 to 255 )
	print(img.shape)	#(256, 256, 3) = resolution
	print(img.size)		#196608
	print(img.ndim)		#3
	print(img)		#[125 137 226] = [Blue Green Red]
					
	
	cv2.imshow('Lena',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__=="__main__":
	main()	



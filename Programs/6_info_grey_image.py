import cv2

def main():
	imgpath="/home/g_r00t/PRIYANK/ex_images/lena_color_256.tif"
	img = cv2.imread(imgpath,0)
		### GREY IMAGE ###
	print(type(img))	#<class 'numpy.ndarray'>
	print(img.dtype)	#uint8  (8 bits = (00000000 to 11111111) = (0x00 to 0xFF) = (0 to 255 )
	print(img.shape)	#(256, 256) = resolutoins
	print(img.size)		#65536
	print(img.ndim)		#2
	print(img)		#[162 161 159] = [0 = BLACK, 255 = WHITE]
					
	
	cv2.imshow('Lena',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__=="__main__":
	main()	



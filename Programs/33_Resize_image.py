import cv2

def main():
	imgpath="/home/g_r00t/PRIYANK/ex_images/4.2.01.tiff"
	img = cv2.imread(imgpath)  #by default value is 1. (0 =for gray scale image, -1 = show colored alpha transperancy image) 
	outpath="/home/g_r00t/PRIYANK/output/shrinked.jpeg"
	outpath1="/home/g_r00t/PRIYANK/output/normal.jpeg"
	outpath2="/home/g_r00t/PRIYANK/output/zoomed.jpeg"
	''''
	output = cv2.resize(img,None,fx=1,fy=1,interpolation=cv2.INTER_LINEAR)
	output1 = cv2.resize(img,None,fx=1,fy=1,interpolation=cv2.INTER_NEAREST)
	output2 = cv2.resize(img,None,fx=1,fy=1,interpolation=cv2.INTER_AREA)
	output3 = cv2.resize(img,None,fx=1,fy=1,interpolation=cv2.INTER_CUBIC)
	output4 = cv2.resize(img,None,fx=1,fy=1,interpolation=cv2.INTER_LANCZOS4)
	'''
	
	output = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LINEAR)
	output1 = cv2.resize(img,None,fx=1,fy=1,interpolation=cv2.INTER_NEAREST)
	output2 = cv2.resize(img,None,fx=5,fy=5,interpolation=cv2.INTER_AREA)
	output3 = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_CUBIC)
	output4 = cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_LANCZOS4)
	
	cv2.imshow('output',output)	
	cv2.imwrite(outpath,output)
	
	cv2.imshow('output1',output1)
	cv2.imwrite(outpath1,output1)
	
	cv2.imshow('output2',output2)
	cv2.imwrite(outpath2,output2)
	
	cv2.imshow('output3',output3)
	cv2.imshow('output4',output4)
	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

if __name__=="__main__":
	main()	

'''
INTER_LINER
INTER_NEATEST
INTER_AREA		- SHIRNKING
INTER_CUBIC		- ZOOMINIG(4X4)
INTER_LANCZ0S4	-(8X8)

'''


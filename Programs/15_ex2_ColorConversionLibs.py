import cv2

def main():
	i=0
	for filename in dir(cv2):
		if filename.startswith('COLOR_'):
			print(filename)
			i=i+1
	print('There are '+ str(i+1) + 'color conversion available in OpenCV')

if __name__=="__main__":
	main()
		
	
'''
some of main color conversion are
1. COLOR_BGR2RGB
2. COLOR_BGR2HSV
3. COLOR_BGR2GRAY
'''	

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path="/home/g_r00t/PRIYANK/ex_images/"
    imgpath1 =  path + "cameraman.tif"

    img = cv2.imread(imgpath1, 0)
 
#    k = np.ones((5, 5), np.uint8)

#    k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
#    k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5, 5))
    k = cv2.getStructuringElement(cv2.MORPH_CROSS,(5, 5))
    
    erosion = cv2.erode(img, k, iterations = 5)
    
    dilation = cv2.dilate(img, k, iterations = 5)
    
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)
    
    print(k)
    
    output = [img, erosion, dilation, gradient]
    
    titles = ['Original', 'Erosion', 'Dilation', 'Gradient']
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        plt.imshow(output[i], cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  

if __name__ == "__main__":
	main()

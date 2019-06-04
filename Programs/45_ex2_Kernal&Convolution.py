import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path="/home/g_r00t/PRIYANK/ex_images/"
    imgpath =  path + "4.2.01.tiff"
    
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    
    k1= np.array(([0, 0, 0], [0, 1, 0],[0, 0, 0]), np.float32)
    k2= np.array(([1, 0, -1], [0, 0, 0], [-1, 0, 1]), np.float32)
    k3= np.array(([0, 1, 0], [1, -4, 1], [0, 1, 0]), np.float32)
    k4= np.array(([-1, -1, -1], [-1, 8, -1],[-1, -1, -1]), np.float32)
    k5= np.array(([0, -1, 0], [-1, 5, -1], [0, -1, 0]), np.float32)
    k6 = np.array(np.ones((11, 11), np.float32))/121
    k7= np.array(([1,2,1], [2,4,2], [1,2,1]), np.float32)/16
   
    output1 = cv2.filter2D(img, -1, k1)
    output2 = cv2.filter2D(img, -1, k2)
    output3 = cv2.filter2D(img, -1, k3)
    output4 = cv2.filter2D(img, -1, k4)
    output5 = cv2.filter2D(img, -1, k5)
    output6 = cv2.filter2D(img, -1, k6)
    output7 = cv2.filter2D(img, -1, k7)
    
    output = [output1,output2,output3,output4,output5,output6,output7]
    result= ['original','Edge dtection 1','Edge dtection 2','Edge dtection 3','sharpen','box blur(normalization)','box blur(Gaussian blur(3x3))']
    for i in range(7):
    	plt.subplot(3, 3, i+1)
    	plt.imshow(output[i])
    	plt.title(result[i])
    	plt.axis('off')
      
    plt.show()

if __name__ == "__main__":
    main()

import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path="/home/g_r00t/PRIYANK/ex_images/"
    imgpath =  path + "house.tiff"

    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    Z = img.reshape((-1,3))
    Z = np.float32(Z)
    
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    k=0
    
    plt.subplot(3,4,1)
    plt.imshow(img)
    plt.title("Original")
    plt.axis("off")
        
    for i in range(1,12):
    	k = k+2
    	print("k =", k)
    	ret, label1, center1 = cv2.kmeans(Z, k, None,
                                      criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    	center1 = np.uint8(center1)
    	res1 = center1[label1.flatten()]
    	output = res1.reshape((img.shape))
    		
    	titles = ['K=24','K=2', 'K=4', 'K=6', 'K=8', 'K=10', 'K=12', 'K=14', 'K=16', 'K=18', 'K=20', 'K=22']	
    	plt.subplot(3,4,i+1)
    	plt.imshow(output)
    	plt.title(titles[i])
    	plt.axis("off")
    	#print('value of i=', i)
    	#print(output)
    plt.show()
    
if __name__=="__main__":
	main()


import cv2
import matplotlib.pyplot as plt
import numpy as np

def main():
    
    path="/home/g_r00t/PRIYANK/ex_images/"
    imgpath1 =  path + "4.2.01.tiff"
    img1 = cv2.imread(imgpath1, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    
    
    rows, columns, channels = img1.shape
    
    point1 = np.float32([[500, 100], [200, 400], [100, 100]])
    point2 = np.float32([[200, 150], [100, 150], [400, 500]])
    
    A = cv2.getAffineTransform(point1, point2)
    
    print(A)
    
    
    output = cv2.warpAffine(img1, A, (columns, rows))
    
    
    plt.imshow(output)
    plt.title('Transformed Image')
    plt.show()

if __name__ == "__main__":
    main()

import cv2
import matplotlib.pyplot as plt

def main():
    
    path="/home/g_r00t/PRIYANK/ex_images/"
    imgpath =  path + "4.2.07.tiff"
    img = cv2.imread(imgpath, 0)
      
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Image')
    plt.xticks([])
    plt.yticks([])
    
    plt.subplot(1, 2, 2)
    plt.hist(img.ravel(), 256, [0, 255])
    plt.title('Histogram')
    plt.xlim(xmin=0, xmax=256)
    plt.show()

if __name__ == "__main__":
    main()

import cv2
import matplotlib.pyplot as plt

def main():
    
    path="/home/g_r00t/PRIYANK/ex_images/"
    imgpath1 =  path + "5.1.12.tiff"
    img = cv2.imread(imgpath1, 0)
    
#    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    block_size = 51
    constant = 2
    th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
    th2 = cv2.adaptiveThreshold (img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_size, constant)
    
    output = [img, th1, th2]
    
    titles = ['Original', 'Mean Adaptive', 'Gaussian Adaptive']
    
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(output[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()  

if __name__ == "__main__":
    main()

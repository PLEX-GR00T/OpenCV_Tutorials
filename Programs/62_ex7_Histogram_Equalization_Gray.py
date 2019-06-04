import cv2
import matplotlib.pyplot as plt

def main():
    
    path="/home/g_r00t/PRIYANK/ex_images/"
    imgpath =  path + "lena_color_512.tif"

    img = cv2.imread(imgpath, 0)
    #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    output1 = cv2.equalizeHist(img)
	
	
    clahe = cv2.createCLAHE()
    clahe1 = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

    output4 = clahe1.apply(img)
    output2 = clahe.apply(img)
	

    output = [img, output1, output2, output4]
    
    titles = ['Original Image', 'Adjusted Histogram', 'CLAHE', 'CLAHE1']
    
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(output[i],cmap='gray')
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()

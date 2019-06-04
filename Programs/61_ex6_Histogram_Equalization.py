import cv2
import matplotlib.pyplot as plt

def main():
    
    path="/home/g_r00t/PRIYANK/ex_images/"
    imgpath =  path + "lena_color_512.tif"

    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    R, G, B = cv2.split(img)
    
    output1_R = cv2.equalizeHist(R)
    output1_G = cv2.equalizeHist(G)
    output1_B = cv2.equalizeHist(B)
    output1 = cv2.merge((output1_R, output1_G, output1_B))
	
	
    clahe = cv2.createCLAHE()
    clahe1 = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

    output2_R = clahe.apply(R)
    output2_G = clahe.apply(G)
    output2_B = clahe.apply(B)
    
    output21_R = clahe1.apply(R)
    output21_G = clahe1.apply(G)
    output21_B = clahe1.apply(B)
    output4 = cv2.merge((output21_R, output21_G, output21_B))
    output2 = cv2.merge((output2_R, output2_G, output2_B))
	

    output = [img, output1, output2, output4]
    
    titles = ['Original Image', 'Adjusted Histogram', 'CLAHE', 'CLAHE1']
    
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])
    plt.show()

if __name__ == "__main__":
    main()

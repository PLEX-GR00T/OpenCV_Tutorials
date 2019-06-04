import cv2

def main():
    	
    #-------------------------------------video of internal webcam-----------------------------------

    windowName = "Live video feed"
    cv2.namedWindow(windowName)
    
    Regular = "video feed"
    cv2.namedWindow(Regular)
    
    cap = cv2.VideoCapture(0)

    filename_reg = "/home/g_r00t/PRIYANK/output/intr_BGR_Form.avi"
    dcode_reg = cv2.VideoWriter_fourcc('X','V','I','D')  # fourCC= four character code, (WMV2,WMV1,MJPG,DIVX,XVID,H264)
    framerate_reg = 30
    resolution_reg = (640,480)
    VideoFileOutput_reg = cv2.VideoWriter(filename_reg, dcode_reg, framerate_reg, resolution_reg)

    filename_nreg = "/home/g_r00t/PRIYANK/output/intr_RGB_Form.avi"
    dcode_nreg = cv2.VideoWriter_fourcc('X','V','I','D')
    framerate_nreg = 30
    resolution_nreg = (640,480)
    VideoFileOutput_nreg = cv2.VideoWriter(filename_nreg, dcode_nreg, framerate_nreg, resolution_nreg)

    if cap.isOpened():
        ret,frame = cap.read()
    else:
        ret = False

    while ret:
        ret,frame= cap.read()
        output = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        VideoFileOutput_reg.write(frame) 
        cv2.imshow (Regular, frame)   

        VideoFileOutput_nreg.write(output)
        cv2.imshow(windowName,output)

        if cv2.waitKey(1)==27:
            break

    cv2.destroyWindow(windowName)
    cv2.destroyWindow(Regular)
    VideoFileOutput_reg.release()
    VideoFileOutput_nreg.release()
    cap.release()

	# --------------------------------------video of external cam1--------------------------------------

    windowName1 = "Live video1 Capturing"
    cv2.namedWindow(windowName1)
    
    Regular1 = "Regular Video"
    cv2.namedWindow(Regular1)

    cap1 =cv2.VideoCapture(1)

    filename_reg1 = "/home/g_r00t/PRIYANK/output/outer_BGR_Form.avi"
    dcode_reg1 = cv2.VideoWriter_fourcc('X','V','I','D')
    framerate_reg1 = 30
    resolution_reg1 = (640,480)
    VideoFileOutput_reg1 = cv2.VideoWriter(filename_reg1, dcode_reg1, framerate_reg1, resolution_reg1)

    filename_nreg1 = "/home/g_r00t/PRIYANK/output/outer_HSV_Form.avi"
    dcode_nreg1 = cv2.VideoWriter_fourcc('X','V','I','D')
    framerate_nreg1 = 30
    resolution_nreg1 = (640,480)
    VideoFileOutput_nreg1 = cv2.VideoWriter(filename_nreg1, dcode_nreg1, framerate_nreg1, resolution_nreg1)

    if cap1.isOpened():
        ret1,frame1 = cap1.read()
    else:
        ret1 = False
    
    while ret1:
        ret1,frame1= cap1.read()
        output1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)    
        
        VideoFileOutput_reg1.write(frame)
        cv2.imshow ('Regular1', frame1)

        VideoFileOutput_nreg1.write(output1)
        cv2.imshow(windowName1,output1)

        if cv2.waitKey(1)==27:
            break

    cv2.destroyWindow(windowName1)
    cv2.destroyWindow(Regular1)
    VideoFileOutput_reg1.release()
    VideoFileOutput_nreg1.release()
    cap1.release()

if __name__== "__main__":
    main() 
    
    
    
    

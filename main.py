import cv2
import numpy as np
import rembg
import time

image = cv2.imread(r"C:\Users\jatin\Downloads\drive-download-20221226T111755Z-001\TEST IMAGES\1.jpg")
# image = cv2.imread(r"C:\Users\jatin\Downloads\drive-download-20221226T111755Z-001\TEST IMAGES\2.jpg")

image.shape
width = image.shape[1]
height = image.shape[0]
black_img = np.zeros((height+50, width, 3), np.uint8)
black_img.shape
text_img = cv2.putText(black_img, "Select an area and Press 'Space key'", (int(width/2)-300, 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
text_img[50:, :, :] = image
kernel = np.ones((2,2),np.uint8)
flag = True

while flag: 
    cv2.namedWindow("select the area", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("select the area", 1080, 720)
    roi = cv2.selectROI("select the area", text_img, showCrosshair = False)
    cv2.destroyWindow("select the area")
    try:
        cropped_image = image[int(roi[1]):int(roi[1]+roi[3]),
                              int(roi[0]):int(roi[0]+roi[2])]
        new_img = rembg.remove(cropped_image)
        roi_img = cv2.cvtColor(new_img,cv2.COLOR_BGR2GRAY)
        roi_img = cv2.dilate(roi_img, kernel, iterations = 10)
        roi_img = cv2.GaussianBlur(roi_img, (15, 15), 0)
        ret, roi_img = cv2.threshold(roi_img, 0, 255, 0)
        roi_img = cv2.morphologyEx(roi_img, cv2.MORPH_GRADIENT, kernel)
        contours, hierarchy = cv2.findContours(roi_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour_img = image.copy()
        for i in range(len(contours)):
            if hierarchy[0][i][3] == -1:
                cv2.drawContours(contour_img, contours, i, (0, 255, 0), 10, offset=(int(roi[0]), int(roi[1])))
        cv2.namedWindow("OUTLINED OBJECT", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("OUTLINED OBJECT", 1080, 720)
        cv2.imshow("OUTLINED OBJECT", contour_img)
    except Exception as e:
        print(e)
    
    
    if cv2.waitKey(0) & 0xFF == ord('c'):
        cv2.destroyWindow("OUTLINED OBJECT")
        cv2.namedWindow("Normal Image", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Normal Image", 1080, 720)
        cv2.imshow("Normal Image", image)
        
    if cv2.waitKey(0) & 0xFF == ord('q'):
        flag = False
        cv2.destroyAllWindows()

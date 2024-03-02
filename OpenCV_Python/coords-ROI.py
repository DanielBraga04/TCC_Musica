import cv2

def showImage(img):
    global obj_img

    obj_img = cv2.imread(img)

    #ROI
    roi = cv2.selectROI(obj_img)
    print(roi)
    im_cropped = obj_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    #cv2.namedWindow("Image")
    #cv2.setMouseCallback("Image", Capture_Event)
    #cv2.imshow("Image", obj_img)

    #MOSTRAR ROI
    cv2.imshow("Cropped Image", im_cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    img = "./img/partitura.png"
    showImage(img)
    

if __name__ == "__main__":
    main()

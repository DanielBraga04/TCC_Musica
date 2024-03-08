import cv2
import numpy as np

#FEITO PELO WILLIANS

def showImage(img):
    global obj_img

    obj_img = cv2.imread(img)

    # ROI
    roi = cv2.selectROI(obj_img)
    print(roi)
    im_cropped = obj_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    # Mostrar ROI
    cv2.imshow("Cropped Image", im_cropped)

    # Converter a imagem para escala de cinza
    gray_im_cropped = cv2.cvtColor(im_cropped, cv2.COLOR_BGR2GRAY)

    # Binarizar a imagem (pixels brancos tornam-se 1, pixels pretos tornam-se 0)
    binary_array = np.where(gray_im_cropped > 128, 1, 0)

    # Converter o array binário de volta para uma imagem
    reconstructed_image = np.zeros_like(gray_im_cropped, dtype=np.uint8)
    reconstructed_image[binary_array == 1] = 255

    # Mostrar a imagem binarizada e reconstruída
    cv2.imshow("Binary Image", reconstructed_image)
    print(binary_array)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    img = "./img/partitura.png"
    showImage(img)

if __name__ == "__main__":
    main()

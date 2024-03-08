import cv2
import numpy as np

#FEITO PELO DANIEL

def showImage(img):

    obj_img = cv2.imread(img)

    #ROI
    roi = cv2.selectROI(obj_img)
    print(roi)
    im_cropped = obj_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    # Converte a área selecionada para escala de cinza
    gray_area = cv2.cvtColor(im_cropped, cv2.COLOR_BGR2GRAY)

    # Cria um array binário onde 0 é branco e 1 é preto
    binary_array = np.where(gray_area == 255, 1, 0)

    print(binary_array)

    reconstruir(binary_array)

    #MOSTRAR ROI
    #cv2.imshow("Cropped Image", im_cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def reconstruir(binario):

    largura, altura = binario.shape
    
    print("Dimensões para a reconstrução: " + str(largura) + "x" + str(altura))

    reconstructed_image = np.zeros((largura, altura, 3), dtype=np.uint8)
    reconstructed_image[:, :, 0] = binario * 255  # Canal azul
    reconstructed_image[:, :, 1] = binario * 255  # Canal verde
    reconstructed_image[:, :, 2] = binario * 255  # Canal vermelho

    #print(reconstructed_image)

    cv2.imshow("Reconstructed Image", reconstructed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#FUNÇÃO PRINCIPAL
def main():
    img = "./img/partitura.png"
    showImage(img)
    

if __name__ == "__main__":
    main()

import cv2
import random
import numpy as np

#Importando a classe RAM
from ram import RAM
from discriminador import Driscriminador

QntPixels = 0

def binarize_image(image):
    # Converter a imagem para escala de cinza
    gray_im_cropped = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binarizar a imagem (pixels brancos tornam-se 1, pixels pretos tornam-se 0)
    binary_array = np.where(gray_im_cropped > 128, 1, 0)

    # Converter o array binário de volta para uma imagem
    reconstructed_image = np.zeros_like(gray_im_cropped, dtype=np.uint8)
    reconstructed_image[binary_array == 1] = 255

    return reconstructed_image

def ROI(img):
    obj_img = cv2.imread(img)

    # ROI
    roi = cv2.selectROI(obj_img)
    #print(roi)
    im_cropped = obj_img[int(roi[1]):int(roi[1] + roi[3]), int(roi[0]):int(roi[0] + roi[2])]

    #Redimensionando para a largura 80 e altura 130
    imagem_redimensionada = cv2.resize(im_cropped, (80, 130))

    #showImage(imagem_redimensionada)

    #Transformando a imagem em binaria
    imagem1_bin = binarize_image(imagem_redimensionada)

    #Mostra a imagem binária
    showImage(imagem1_bin)

    #Função que irá pegar os pixels aleatórios
    pixelAleatorio(imagem1_bin)

def inverter_valor(valor):
    if valor == 0: # Se o valor for 0 (preto), retorna 1
        return 1
    else: # Se o valor for diferente de 0 (branco), retorna 0
        return 0

def pixelAleatorio(imagem):
    global QntPixels

    height, width = imagem.shape[:2]

    # Definir o número de pixels aleatórios a serem escolhidos
    num_random_pixels = width * height

    QntPixels = num_random_pixels

    # Escolher pixels aleatórios
    random_pixels = [(random.randint(0, height - 1), random.randint(0, width - 1)) for _ in range(num_random_pixels)]

    #Cria uma cópia da lista dos pixels aleatórios
    random_pixel_order = random_pixels.copy()

    #print("Ordem dos pixels sorteados e seus valores binários na imagem1:")
    #print("")
    #for i, pixel in enumerate(random_pixel_order):
        #valor_invertido = inverter_valor(imagem[pixel])
        #print(f"Índice: ({pixel[1]}, {pixel[0]}), Valor: {valor_invertido}")

def showImage(img):
    #MOSTRAR ROI
    cv2.imshow("Cropped Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#FUNÇÃO MAIN
def main():
    global QntPixels
    img = "./img/partitura.png"
    #obj_img = cv2.imread(img)
    ROI(img)

    #pixelAleatorio(obj_img)

    discri = Driscriminador()

    nBits = 3

    total_bits = QntPixels * nBits
    # Criar e adicionar as RAMs ao Discriminador
    for _ in range(total_bits):
        ram = RAM(indice=None, nbits=nBits)
        discri.adicionar_ram(ram)

    print(f"Foram criadas e adicionadas {total_bits} RAMs ao discriminador.")
    

if __name__ == "__main__":
    main()
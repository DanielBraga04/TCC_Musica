#Importando bibliotecas uteis
import cv2
import random
import numpy as np

#Importando a classe RAM
from ram import RAM
from discriminador import Driscriminador

qntPixels = 0
ordemAleatoria = 0

def binarize_image(image):
    # Converter a imagem para escala de cinza
    gray_im_cropped = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binarizar a imagem (pixels brancos tornam-se 1, pixels pretos tornam-se 0)
    binary_array = np.where(gray_im_cropped > 128, 1, 0)

    # Converter o array binário de volta para uma imagem
    reconstructed_image = np.zeros_like(gray_im_cropped, dtype=np.uint8)
    reconstructed_image[binary_array == 1] = 255

    return reconstructed_image

def ROI(img, nBits):
    obj_img = cv2.imread(img)

    nBitsROI = nBits

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
    pixelAleatorio(imagem1_bin, nBitsROI)

def inverter_valor(valor):
    if valor == 0: # Se o valor for 0 (preto), retorna 1
        return 1
    else: # Se o valor for diferente de 0 (branco), retorna 0
        return 0

def pixelAleatorio(imagem, nBits):
    global qntPixels
    global ordemAleatoria

    height, width = imagem.shape[:2]

    qntPixels = width * height

    # Embaralhar os índices dos pixels
    random_pixels_indices = list(range(width * height))
    random.shuffle(random_pixels_indices)

    # Escolher pixels aleatórios na ordem embaralhada
    random_pixel_order = [(index // width, index % width) for index in random_pixels_indices]

    ordemAleatoria = random_pixel_order.copy()

    #print("Ordem dos pixels sorteados e seus valores binários na imagem1:")
    for i, pixel in enumerate(random_pixel_order):
        valor_invertido = inverter_valor(imagem[pixel])
        #print(f"Índice: ({pixel[1]}, {pixel[0]}), Valor: {valor_invertido}")

    int_values = []

    # Converter cada grupo de nBits em um número inteiro
    current_value = 0
    bits_count = 0
    for i, pixel in enumerate(random_pixel_order):
        valor_invertido = inverter_valor(imagem[pixel])
        # Adicionar o bit invertido ao valor atual
        current_value = (current_value << 1) | valor_invertido
        bits_count += 1
        # Se atingirmos o número de bits necessário, adicione o valor inteiro à lista
        if bits_count == nBits:
            int_values.append(current_value)
            current_value = 0
            bits_count = 0

    # Imprimir os valores inteiros
    #print("")
    #print("Valores inteiros:")
    #for i, value in enumerate(int_values):
        #print(f"Índice: {i}, Valor: {value}")

    return int_values

def similarImagem(imagem, nBits):

    #print("")
    #print("Ordem dos pixels sorteados e seus valores binários na imagem similada:")
    for i, pixel in enumerate(ordemAleatoria):
        valor_invertido = inverter_valor(imagem[pixel])
        #print(f"Índice: ({pixel[1]}, {pixel[0]}), Valor: {valor_invertido}")

    int_values = []

    # Converter cada grupo de nBits em um número inteiro
    current_value = 0
    bits_count = 0
    for i, pixel in enumerate(ordemAleatoria):
        valor_invertido = inverter_valor(imagem[pixel])
        # Adicionar o bit invertido ao valor atual
        current_value = (current_value << 1) | valor_invertido
        bits_count += 1
        # Se atingirmos o número de bits necessário, adicione o valor inteiro à lista
        if bits_count == nBits:
            int_values.append(current_value)
            current_value = 0
            bits_count = 0

    return int_values

def showImage(img):
    #MOSTRAR ROI
    cv2.imshow("Cropped Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


#FUNÇÃO MAIN
def main():
    global QntPixels
    #IMAGEM DE TESTE PARA VÊ SE TÁ FUNCIONANDO O CÓDIGO
    img = "./img/imagem_teste.png"
    obj_img = cv2.imread(img)

    img2 = "./img/imagem_teste2.png"
    obj_img2 = cv2.imread(img2)

    nBits = 5

    #ROI(img, nBits)

    binario = binarize_image(obj_img)
    binario_similar = binarize_image(obj_img2)

    endereco = pixelAleatorio(binario, nBits)
    endereco2 = similarImagem(binario_similar, nBits)

    discri = Driscriminador()
    discri2 = Driscriminador()

    total_bits = int(qntPixels / nBits)

    discri.criar_e_adicionar_rams(total_bits, nBits)
    discri2.criar_e_adicionar_rams(total_bits, nBits)

    #print(f"Foram criadas e adicionadas {total_bits} RAMs ao discriminador.")

    discri.incrementar(endereco)

    print()
    print("Endereço dado da imagem 1: ", endereco)
    print()
    print("A lista do discriminador 1 temos: ")
    discri.imprimir_rams()

    discri2.incrementar(endereco2)

    print()
    print("Endereço dado da imagem 2: ", endereco2)
    print()
    print("A lista do discriminador 2 temos: ")
    discri2.imprimir_rams()

    similaridade = discri.calcular_similaridade(discri2)
    print(f"A similaridade entre os discriminadores é: {similaridade:.2f}%")

if __name__ == "__main__":
    main()
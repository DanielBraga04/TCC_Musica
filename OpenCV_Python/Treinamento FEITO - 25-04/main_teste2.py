#Importando bibliotecas uteis
import cv2
import random
import numpy as np
import os
from discriminador import Discriminador
from ram import RAM

#Importando a classe RAM



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

def redimensionar(img):

    imagem_redimensionada = cv2.resize(img, (80, 130))

    return imagem_redimensionada

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

def carregar_imagens_diretorio(diretorio):
    imagens = []
    for filename in os.listdir(diretorio):
        if filename.endswith(".png") or filename.endswith(".jpg"):
            img_path = os.path.join(diretorio, filename)
            image = cv2.imread(img_path)
            #Redimensionar a imagem para a largura e altura desejadas
            resized_image = cv2.resize(image, (80, 130))
            imagens.append(resized_image)
    return imagens

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

    #print("Ordem dos pixels sorteados e seus valores binários na imagens:")
    #for i, pixel in enumerate(random_pixel_order):
        #valor_invertido = inverter_valor(imagem[pixel])
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
    global qntPixels
    #IMAGEM DE TESTE PARA VÊ SE TÁ FUNCIONANDO O CÓDIGO
    diretorio_imagens_sol = "./ClaveSol/"
    imagens_sol = carregar_imagens_diretorio(diretorio_imagens_sol)

    diretorio_imagens_fa = "./ClaveFa/"
    imagens_fa = carregar_imagens_diretorio(diretorio_imagens_fa)

    imagem_trei = "./img/clave_treinamento_4.png"
    obj_trei = cv2.imread(imagem_trei)

    nBits = 4

    total_bits = int((80 * 130) / nBits)

    discri_sol = Discriminador()
    discri_sol.criar_e_adicionar_rams(total_bits, nBits)

    discri_fa = Discriminador()
    discri_fa.criar_e_adicionar_rams(total_bits, nBits)

    discri_trei = Discriminador()
    discri_trei.criar_e_adicionar_rams(total_bits, nBits)

    for i, img in enumerate(imagens_sol):
        img_red_sol = redimensionar(img)
        binario = binarize_image(img_red_sol)
        endereco_sol = pixelAleatorio(binario, nBits)
        discri_sol.incluir_endereco(endereco_sol)
        print(f"Endereços dados de SOL {i+1}: ", endereco_sol)

    print("")
    for i, img in enumerate(imagens_fa):
        img_red_fa = redimensionar(img)
        binario = binarize_image(img_red_fa)
        endereco_fa = pixelAleatorio(binario, nBits)
        discri_fa.incluir_endereco(endereco_fa)
        print(f"Endereços dados de FÁ {i+1}: ", endereco_fa)

    img_red_trei = redimensionar(obj_trei)
    bi_trei = binarize_image(img_red_trei)
    endereco_trei = similarImagem(bi_trei, nBits)
    discri_trei.incluir_endereco(endereco_trei)


    print("--------------------------------------------------")
    print("")

    print("RAMs DO DISCRI DE SOL")
    discri_sol.imprimir_rams()

    print("--------------------------------------------------")
    print("")

    print("RAMs DO DISCRI DE FÁ")
    discri_fa.imprimir_rams()

    print("--------------------------------------------------")
    print("")

    print("RAMs DO DISCRI DE TREINO")
    discri_trei.imprimir_rams()

    discri_trei.calcular_similaridade_2(discri_sol, discri_fa)




if __name__ == "__main__":
    main()
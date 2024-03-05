import cv2
import numpy as np

def showImage(img):

    obj_img = cv2.imread(img)

    #ROI
    roi = cv2.selectROI(obj_img)
    print(roi)
    im_cropped = obj_img[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    #MOSTRAR ROI
    cv2.imshow("Cropped Image", im_cropped)

    #CHAMANDO A FUNÇÃO DOS PIXELS
    pixels(im_cropped)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def pixels(img):
    #retorna uma tupla que contém as dimensões da imagem. como: altura, largura e os canais de cores (BGR)
    altura, largura, canais_cor = img.shape
    print("Dimensões da imagem: " + str(altura) + "x" + str(largura))

    #Criando a matriz
    matriz = np.zeros((altura, largura), dtype=np.uint8)
    #np.zeros - cria uma matriz preenchida com zeros. altura e largura seria o tamanho da matriz.
    #dtype=np.uint8 - tipo de dados numérico sem sinal de 8 bits, o que significa que ele pode armazenar valores inteiros de 0 a 255.
    
    #Percorrendo a imagem/matriz
    for x in range(0, altura):
        for y in range(0, largura):

            azul, vermelho, verde = getColor(img, x, y)

            if azul == 0 and vermelho == 0 and verde == 0:
                #print("[" + str(x) + "x" + str(y) + "] pixel é preto")
                matriz[x][y] = 1
            #else:
                #print("[" + str(x) + "x" + str(y) + "] pixel é branco")
                #matriz[x][y] = 0

    print(matriz)
                
#FUNÇÃO QUE DÁ QUAL É A INTENSIDADE DO BGR OU RGB. Utilizando o comando ".item()"
def getColor(image, x, y):
    return image.item(x, y, 0), image.item(x, y, 1), image.item(x, y ,2)

#FUNÇÃO PRINCIPAL
def main():
    img = "./img/partitura.png"
    showImage(img)
    

if __name__ == "__main__":
    main()
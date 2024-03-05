import cv2
import numpy as np

def pixels(img):
    altura, largura, canais_cor = img.shape
    print("Dimensões da imagem: " + str(largura) + "x" + str(altura))

    matriz = np.zeros((altura, largura), dtype=np.uint8)
    
    for x in range(0, altura):
        for y in range(0, largura):
            #print("[" + str(x) + "," + str(y) + "] = " + str(img[y][x]))

            azul, vermelho, verde = getColor(img, x, y)

            if azul == 0 and vermelho == 0 and verde == 0:
                #print("[" + str(x) + "x" + str(y) + "] pixel é preto")
                matriz[x][y] = 1
            else:
                #print("[" + str(x) + "x" + str(y) + "] pixel é branco")
                matriz[x][y] = 0
    
    print(matriz)

def getColor(image, x, y):
    return image.item(x, y, 0), image.item(x, y, 1), image.item(x, y ,2)

def showImage(img):

    obj_img = cv2.imread(img)

    #chamando a função pixels
    pixels(obj_img)

    cv2.imshow("Image", obj_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    img = "./img/imagem.png"
    showImage(img)

if __name__ == "__main__":
    main()
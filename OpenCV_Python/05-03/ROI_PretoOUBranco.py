import cv2

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
    altura, largura, canais_cor = img.shape
    print("Dimensões da imagem: " + str(largura) + "x" + str(altura))
    
    for x in range(0, altura):
        for y in range(0, largura):
            #print("[" + str(x) + "," + str(y) + "] = " + str(img[y][x]))

            azul, vermelho, verde = getColor(img, x, y)

            if azul == 0 and vermelho == 0 and verde == 0:
                print("[" + str(x) + "x" + str(y) + "] pixel é preto")
            else:
                print("[" + str(x) + "x" + str(y) + "] pixel é branco")

def getColor(image, x, y):
    return image.item(x, y, 0), image.item(x, y, 1), image.item(x, y ,2)

def main():
    img = "./img/partitura.png"
    showImage(img)
    

if __name__ == "__main__":
    main()
import cv2
import os

def redimensionar(diretorio, altura_desejada):
    imagens_originais = []
    imagems_redimensionadas = []

    # Leitura das imagens e redimensionamento
    for filename in sorted(os.listdir(diretorio)):
        if filename.endswith(".png"):
        # Lendo a imagem
            imagem = cv2.imread(os.path.join(diretorio, filename))
        
        # Obtendo as dimensões originais da imagem
            altura_original, largura_original = imagem.shape[:2]
        
        # Calculando o fator de escala para redimensionar a imagem para a altura desejada
            fator_escala = altura_desejada / altura_original
        
        # Redimensionando a imagem mantendo a proporção
            imagem_redimensionada = cv2.resize(imagem, (int(largura_original * fator_escala), altura_desejada))

        # Colocando as imagens nos vetores
            imagens_originais.append(imagem)
            imagems_redimensionadas.append(imagem_redimensionada)
        
    return imagems_redimensionadas, imagens_originais


def mostrar_imagem(imagens_red, imagens_ori):
    # Mostrar as imagens originais
    #for i, imagem in enumerate(imagens_ori):
    #    cv2.imshow(f"Imagem Original {i+1}", imagem)

    # Mostrar as imagens redimensioandas
    for i, imagem in enumerate(imagens_red):
        cv2.imshow(f"Imagem Redimensionadas {i+1}", imagem)
        # Esperar até que uma tecla seja pressionada para fechar as janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def main():
    diretorio = './ClaveSol/'
    altura_desejada = 100
    img_redimensionada, img_originais = redimensionar(diretorio, altura_desejada)
    mostrar_imagem(img_redimensionada, img_originais)

if __name__ == "__main__":
    main()
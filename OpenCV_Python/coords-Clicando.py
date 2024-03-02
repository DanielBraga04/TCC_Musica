import cv2

clicked_points = []

def Capture_Event(event, x, y, flags, params):
    global clicked_points

    if event == cv2.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))

        if len(clicked_points) == 2:
            # Mostra as coordenadas dos dois cliques
            print("Coordenadas do primeiro clique:", clicked_points[0])
            print("Coordenadas do segundo clique:", clicked_points[1])
            print("")

            cv2.rectangle(obj_img, clicked_points[0], clicked_points[1], (0, 0, 255), 2)

            cv2.imshow("Image", obj_img)

            # Limpa a lista para que novos cliques possam ser registrados
            clicked_points.clear()

        #print(f"({x}, {y})")

def showImage(img):
    global obj_img

    obj_img = cv2.imread(img)
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", Capture_Event)
    cv2.imshow("Image", obj_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    img = "./img/partitura.png"
    showImage(img)
    

if __name__ == "__main__":
    main()
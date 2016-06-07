import cv2

def main():
    camera = cv2.VideoCapture(0)

    cv2.namedWindow('Camera', cv2.WINDOW_AUTOSIZE)

    num = 0
    while True:
        ret, image = camera.read()
        if ret == False:
            continue

        cv2.imshow('Camera', image)

        if cv2.waitKey(33) >= 0:
            cv2.imwrite('.\carib\%d.jpg'% num, image)
            num += 1


    cv2.destroyAllWindows()




if __name__=='__main__':
    main()

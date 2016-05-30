import cv2

if __name__=="__main__":

		capture = cv2.VideoCapture(0)

		if capture.isOpened() is False:
				print("Camera is not find")
		
		cv2.namedWindow("MagoRock", cv2.WINDOW_AUTOSIZE)

		while True :

				ret, image = capture.read()

				if ret == False:
						continue

				cv2.imshow("MagoRock", image)

				if cv2.waitKey(33) >= 0:
						cv2.imwrite("image.png", image)
						break

		cv2.destroyAllWindows

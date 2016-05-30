import cv2

if __name__=="__main__":

		image = cv2.imread('image.png')
		cut_image = image[150:250, 375:475]

		cv2.imshow('mago',cut_image)
		cv2.waitKey(0)
		cv2.imwrite('cut_image.png', cut_image)
		cv2.destroyAllWindows()

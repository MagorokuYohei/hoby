import cv2
import numpy as np
from matplotlib import pyplot as plt

if __name__=="__main__":

		img    = cv2.imread("image.png")
		img_gry= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		ct_img = cv2.imread("cut_image.png", 0)
		w, h = ct_img.shape[::-1]

		res = cv2.matchTemplate(img_gry, ct_img, cv2.TM_CCOEFF_NORMED)
		threshold = 0.8
		loc = np.where( res >= threshold)

		for pt in zip(*loc[::-1]):
				cv2.rectangle(img, pt, (pt[0] +w, pt[1]+h),(0,0,0), 2)


		cv2.imshow("img",img)
		cv2.imshow("ct_img",ct_img)

		cv2.waitKey(0)
		cv2.destroyAllWindows()

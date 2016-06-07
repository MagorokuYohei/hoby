#-*-coding:utf-8-*-

import numpy
import cv2
from glob import glob
import Tkinter
import tkMessageBox

def main():
    square_size = 2.0
    pattern_size = (10, 7)
    pattern_points = numpy.zeros( (numpy.prod(pattern_size), 3), numpy.float32)
    pattern_points[:,:2] = numpy.indices(pattern_size).T.reshape(-1,2)
    pattern_points *= square_size
    obj_points = []
    img_points = []

    for fn in glob(".\carib\*.jpg"):
        im = cv2.imread(fn, 0)
        found, corner = cv2.findChessboardCorners(im, pattern_size)
        if found:
            term = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_COUNT, 30, 0.1)
            cv2.cornerSubPix(im, corner, (5,5), (-1,-1), term)
            cv2.drawChessboardCorners(im,pattern_size, corner, found)
            cv2.imshow('corners '+fn, im)
        if not found:
            print 'Not found chessboard' + fn
            continue
        root = Tkinter.Tk()
        root.withdraw()

        if tkMessageBox.askyesno('askyesno','Do you adopt this image?'):
            img_points.append(corner.reshape(-1,2))
            obj_points.append(pattern_points)

        cv2.destroyAllWindows()



    rms, K, d, r, t = cv2.calibrateCamera(obj_points, img_points,(im.shape[1], im.shape[0]))

    print 'RMS =', rms
    print 'K =\n', K
    print 'd =', d.ravel()
    f = open('rms.txt', 'w')
    f.write(str(rms))
    f.close()
    numpy.savetxt(".K.csv", K, delimiter = ',', fmt="%0.14f")






if __name__=='__main__':
    main()

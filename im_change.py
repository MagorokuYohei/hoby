# -*- coding: utf-8 -*-
# -*-coding: utf-8 -*-
import os
import glob
import cv2


def main():
    print "Please input change file extension:"
    print "(Exsample).txt"
    ext = raw_input()
    ext = ".\cafe\*%s" % ext

    print "Please input transport file extension"
    print "Sample A-[num].log"
    print "input part of A"
    head = raw_input()
    print "input part of .extension (.log)"
    trans = raw_input()

    mfile = glob.glob(ext)
#    print mfile
    #os.rename(mfile[0], 'sen.txt')

    ct = 1
    for i in mfile:
        print i
#        os.rename(i, '%s-%s%s' % (head,ct,trans))
        img = cv2.imread(i, 1) # 画像をグレースケールに変換して読み込む
        cv2.imwrite('.\cafe\R\%s-%s%s' % (head,ct,trans), img)
        ct+=1


if  __name__=="__main__":
    main()

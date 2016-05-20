#-*-coding:utf-8-*-
import threading
import time
import datetime


num = 0
class Thread(threading.Thread):

    def __init__(self):
        super(Thread, self).__init__()

    def run(self):
        i=0
        global num
        while(i<10):
            num += 1
            print num
            time.sleep(1)
            i +=1



def main():
    global num
    print num
    th_cl = Thread()
    th_cl.start()
    time.sleep(15)
    print num


if __name__=='__main__':
    main()

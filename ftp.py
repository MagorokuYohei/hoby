#-*-coding:utf-8-*-

from ftplib import FTP
HOST = ''
USER = ''
PASS = ''

def main():
    print "Start"
    ftp = FTP(HOST, USER, PASS)
    ftp.cwd('/SYS/')#送信先のディレクトリ指定
    f = open('./sample.txt', 'rb')#読み込み、バイナリ
    ftp.storbinary('STOR sample.txt', f)#sample.txtをバイナリで送信
    f.close
    ftp.close()
    print "Finish"

if __name__=='__main__':
    main()

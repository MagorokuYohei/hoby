#-*-coding:utf-8-*-

import socket
from contextlib import closing

def main():
    host = '127.0.0.1'
    port = 4000
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

    message = 'HELLO MAGOROCK'
    sock.sendto(message, (host, port))

if __name__=='__main__':
    main()  

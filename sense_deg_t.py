#-*-coding:utf-8-*-
import numpy as np
from matplotlib import pyplot as plt
import seaborn
import random


def main():
    g_deg_x =0
    g_deg_y =0
    g_deg_z =0

    a_deg_x =0
    a_deg_y =0
    a_deg_z =0

    g_deg_x_l = []
    a_deg_x_l = []
    g_deg_y_l = []
    a_deg_y_l = []
    g_deg_z_l = []
    a_deg_z_l = []
    angle_l = []
    num = []
    i=0
    dt = 0.0918174910545
    angle = 0

    mu   = 0
    sigm = 0
    M = []
    R = 0.001
    Q = 0.003


    for line in open('sense_hat.txt', 'r'):
        a = line.split(',')

        _g_deg_x = np.degrees(-float(a[1]))*dt
        _g_deg_y = np.degrees(float(a[0])) *dt
        _g_deg_z = np.degrees(float(a[2])) *dt

        g_deg_x += _g_deg_x
        g_deg_y += _g_deg_y
        g_deg_z += _g_deg_z

        a_deg_x = np.degrees(np.arctan2(float(a[3]), np.sqrt(float(a[4])**2 + float(a[5])**2)))
        a_deg_y = np.degrees(np.arctan2(float(a[4]), np.sqrt(float(a[3])**2 + float(a[5])**2)))
        a_deg_z = np.degrees(np.arctan2(float(a[5]), np.sqrt(float(a[3])**2 + float(a[4])**2)))

        _mu   = mu + _g_deg_x
        _sigm = sigm  + R
        s     = _sigm + Q
        z     = a_deg_x - mu
        K     = _sigm/s
        mu    = _mu + K*z
        sigm  = (1-K)*_sigm

        M.append(mu)


        angle = (0.98)*(angle + _g_deg_x ) + (0.02)*(a_deg_x);
        angle_l.append(angle)

        g_deg_x_l.append(g_deg_x)
        a_deg_x_l.append(a_deg_x)
        g_deg_y_l.append(g_deg_y)
        a_deg_y_l.append(a_deg_y)
        g_deg_z_l.append(g_deg_z)
        a_deg_z_l.append(a_deg_z)
        num.append(i)
        i+=1

    plt.plot(num,g_deg_x_l, 'r-', label='Gyro_X')
    plt.plot(num,a_deg_x_l, 'b-', label='Accel_X')
    plt.plot(num,angle_l, 'g-', label='Simple_Fiter_X')

    plt.plot(num,M, 'k-', label='Kalman_Fiter_X')

#    plt.plot(num,g_deg_y_l, 'y-', label='Gyro_Y')
#    plt.plot(num,a_deg_y_l, 'd-', label='Accel_Y')
    plt.legend()
    plt.show()


if __name__=='__main__':
    main()

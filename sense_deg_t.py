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
    dt =0.0919430088997
    angle = 0

    mu   = 0
    sigm = 0
    M = []
    R = 0.00000051
    Q = 0.000024

    summ = 0
    summ2= 0

    vv  = 0.
    vv2 = 0.


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

        summ += _g_deg_x
        summ2+= a_deg_x

        vv  += (_g_deg_x - 0.000792)**2
        vv2 += (a_deg_x - 5.269212)**2



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

    print "Gyro_ave %f"%(summ/10000.)
    print "Accel_ave %f"%(summ2/10000.)
    print "Gyro_v %f"%(vv/10000.)
    print "Accel_v %f"%(vv2/10000.)


if __name__=='__main__':
    main()

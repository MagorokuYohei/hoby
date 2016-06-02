#-*-coding:utf-8-*-
import xlrd
import numpy as np
from matplotlib import pyplot as plt
import seaborn

def main():
    book = xlrd.open_workbook('sense_hat.xlsx')
    sheet = book.sheet_by_index(0)

    g_deg_x =0
    g_deg_y =0
    g_deg_z =0

    a_deg_x =0
    a_deg_y =0
    a_deg_z =0

    g_deg_x_l = []
    a_deg_x_l = []
    num = []
    for row in range(1, sheet.nrows-1):
        data = []
        for col in range(0, sheet.ncols-2):
            data.append(sheet.cell(row,col).value)
        g_deg_x += np.degrees(data[0])*0.1
        g_deg_y += np.degrees(data[1])*0.1
        g_deg_z += np.degrees(data[2])*0.1

        a_deg_x = np.degrees(np.arctan2(data[3], np.sqrt(data[4]**2 + data[5]**2) ))
        a_deg_y = np.degrees(np.arctan2(data[4], np.sqrt(data[3]**2 + data[5]**2) ))
        a_deg_z = np.degrees(np.arctan2(data[5], np.sqrt(data[3]**2 + data[4]**2) ))

        g_deg_x_l.append(g_deg_x)
        a_deg_x_l.append(a_deg_x)
        num.append(row-1)

    plt.plot(num,g_deg_x_l, 'r-', label='Gyro')
    plt.plot(num,a_deg_x_l, 'b-', label='Accel')
    plt.legend()
    plt.show()




if __name__=='__main__':
    main()

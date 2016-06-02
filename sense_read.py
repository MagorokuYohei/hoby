#-*-coding:utf-8-*-
import xlrd
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn

def main():
    book = xlrd.open_workbook('sense_hat.xlsx')
    sheet = book.sheet_by_index(0)
    date = []
    num  = []
    total = 0.
    for col in range(0,6):
        print sheet.cell(0,col).value
        for row in range(0,sheet.nrows-1):
            num.append(row)
            date.append(sheet.cell(row+1,0).value)
            total += float(sheet.cell(row+1,0).value)
            ave = total/ (sheet.nrows-1)
        print 'Ave: %f'%ave

        V = 0.
        for i in range(0, len(date)):
            V += (ave-date[i])**2
        V = V /len(date)
        print 'V: %f'% V
        mu = np.sqrt(V)
        print 'm: %f'% mu

    plt.axhline(y=0)
    plt.plot(num, date, 'r-')
#    plt.show()


if __name__=='__main__':
    main()

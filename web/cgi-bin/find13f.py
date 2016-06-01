#!/usr/bin/env python
#-*-coding:utf-8-*-
import cgi
from datetime import datetime

def main():
    html_body = u"""
    <html><head>
    <meta http-equiv="content-type" content="text/html;charset=utf-8">
    </head>
    <body>
    %s
    </body></html>"""
    content = ''

    form = cgi.FieldStorage()
    year_str = form.getvalue('year', '')
    if not year_str.isdigit():
        content = u'Please input year'
    else:
        year = int(year_str)
        friday13=0

        for month in range(1,13):
            data = datetime(year, month, 13)
            if data.weekday() == 4:
                friday13 +=1
                content += u'Year:%d Month:%d Day:13 is Friday'%(year, month)
                content += u'<br />'
        if friday13:
                content += u'Year %d has %d Friday'%(year, friday13)
        else:
                content += u'Year %d has not Friday'% year

    print "Content-type: text/html\n"
    print (html_body % content).encode('utf-8')

if __name__=='__main__':
    main()

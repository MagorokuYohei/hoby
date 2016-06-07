#-*-coding:utf-8-*-
import cgi
from datetime import datetime

def main():
    html_body = u"""
    <html>
    <head>
    <meta http-equiv="content-type" content = "text/html;charset=utf-8"/>
    </head>
    <body>
     <form method="POST" action="/cgi-bin/find13f.py">
     Please select year
     <select name="year">
     %s
     </select>
     <input type="submit"/>
     </form>
     %s
    </body>
    </html>"""
    options=''
    content=''

    now = datetime.now()
    for y in range(now.year-10, now.year+10):
        if y!=now.year:
            select =''
        else:
            select = ' selected="selected"'
        options += "<option%s>%d</option>"%(select, y)

    form = cgi.FieldStorage()
    year_str=form.getvalue('year','')
    if year_str.isdigit():
        year=int(year_str)
        friday13=0
        for month in range(1,13):
            date=datetime(year,month,13)
            if date.weekday()==4:
                friday13 +=1
                content += u"%d %d 13 is Friday"%(year,month,)
                content += u"<br />"

        if friday13:
            content += u"%d has &d Fridays"%(year, friday13)
        else:
            content += u"%d has not Friday"%year
    print "Content-type: text/html;charset=utf-8\n"
    print html_body % (options, content)


if __name__=='__main__':
    main()

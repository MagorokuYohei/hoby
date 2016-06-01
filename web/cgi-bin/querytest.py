#!/usr/bin/env python
import cgi

def main():
    html_body = """
    <html><body>
    foo = %s
    </body></html>"""

    form = cgi.FieldStorage()
    print "Content-type: text/html\n"
    print html_body% form.getvalue('foo', 'N/A')
if __name__=='__main__':
    main()

#!/usr/bin/python
import cgi
import json
print "Content-type: text/html\n"
form = cgi.FieldStorage()
todict = json.loads(form.getvalue('file'))
try:
  print("1")
  with open(todict['way'], 'w') as file:
    file.write(todict['datable'])
except IOError as e:
    print("0")

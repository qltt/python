#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import re
import os
import threading
import time 

# os.system('taskkill /f /im Shadowsocks.exe')
website = 'http://ss.ishadowx.com'
#/http://free.ishadow.online
#/http://go.ishadow.online


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getResult(html):
    regName = r'Address:<span id="\w+">(\w+\.\w+\.\w+)<'
    comName = re.compile(regName)
    resName = re.findall(comName,html)

    #r'Port：(\d+)</h4'
    regPort = r'Port:<span id="\w+">(\d+)'
    comPort = re.compile(regPort)
    resPort = re.findall(comPort,html)

    #r'Password:<span id="\w+">(\d+)</span'
    regPass = r'Password:<span id="\w+">(\d+)'
    comPass = re.compile(regPass)
    resPass = re.findall(comPass,html)

    regMeth = r'Method:(.*?)</h4'
    comMeth = re.compile(regMeth)
    resMeth = re.findall(comMeth,html)
    
    #print resName
    #print resPort
    #print resPass
    #print resMeth
    return resName, resPort,resPass, resMeth

def changeLocal(inFo,i=0):
    textLocal=open('C:\Users\Wei\Desktop\gui-config.json','r')
    readText=textLocal.read()
    textLocal.close()

#    print readText
    regName1 = r'"server" : "(\w+\.\w+\.\w+)"'
    comName1 = re.compile(regName1)
    resName1 = re.findall(comName1,readText)

    regPort1 = r'"server_port" : (\d+),'
    comPort1 = re.compile(regPort1)
    resPort1 = re.findall(comPort1,readText)

    regPass1 = r'"password" : "(\d+)"'
    comPass1 = re.compile(regPass1)
    resPass1 = re.findall(comPass1,readText)

    regMeth1 = r'"method" : "(.*?)"'
    comMeth1 = re.compile(regMeth1)
    resMeth1 = re.findall(comMeth1,readText)

    print resName1, resPort1, resPass1
    text1=readText.replace(resName1[0],inFo[0][i]).replace(resPort1[0],inFo[1][i]).replace(resPass1[0],inFo[2][i]).replace(resMeth1[0],inFo[3][i].lower())
#   print text1
    textHand=open('C:\Users\Wei\Desktop\gui-config.json','w')
    textHand.write(text1)
    textHand.close()

def theMain():
	os.system('taskkill /f /im Shadowsocks.exe')
	html = getHtml(website)
    #http://seofangfa.com/shadowsocks.html
	inFo = getResult(html)
	changeLocal(inFo,index)
	os.system('C:\\Users\\Wei\\Desktop\\Shadowsocks.exe')

chra = 'g'
while chra != 'q':
    
    index=int(raw_input('0 or 1 or 2:'))
    t = threading.Thread(target = theMain)
    t.start()
    time.sleep(5)

    chra = raw_input('Get or Quit?(g/q)')
   

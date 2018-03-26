#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import Tkinter
import tkFileDialog
import datetime
from threading import Thread

f = open('test.txt','r')
text = f.read()

# This function is used with class re to search regular express
def findPart(regex, text):
	# regex1 = re.compile(regex, re.S)
	res = re.findall(regex, text)
	if res:
		return res
	else:
		return 'No finding...'

# This part is for encoding between Chinese and normal characters
usample = unicode(text, 'utf8')
print res[0].encode('utf8')

# This function is UI to open file and read the information
def openAndgetFileInfo(explain, format0):
	root = Tkinter.Tk()
	root.withdraw()
	f = tkFileDialog.askopenfile(filetypes = [(explain, format0)])  # 
	fullText = f.read()
	f.close()
	return fullText

def showChoice(stringTitle, stringText):
	return tkMessageBox.askyesno(title = stringTitle, message = stringText)

def showWarning(stringTitle, stringText):
	return tkMessageBox.showwarning(title = stringTitle, message = stringText)

# This function sets a logging file	
def log(logFileName, message):
	import logging as lg
	# logger = lg.getLogger()
	logger1 = lg.getLogger('weiLoger')
	logger1.setLevel(lg.DEBUG)
	fh = lg.FileHandler(logFileName + '.log')
	formatter = lg.Formatter('%(asctime)s - %(name)s \n- %(levelname)s \n-%(message)s \n\n')
	fh.setFormatter(formatter)
	logger1.addHandler(fh)
	logger1.error(message)

'\n'.join(str(i) for i in range(5))

'{} is typed in...'.format(answer)
'%s is typed in...' %(answer)
fileName = 'Result-' + f1 + '-{:0>2}{:0>2}{:0>2}.txt'.format(d.hour,d.minute,d.second)

newString = oldString.replace( old, new)

# This part is for ask save file name with certain format
filename = tkFileDialog.asksaveasfilename(filetypes=[('Save new ssi file','.ssi')], title = 'Set new ssi file path and name')
if '.ssi' not in filename:
	filename += '.ssi'
with open(filename + '.ssi','wb') as wf:
	wf.write(all_info)


# This part is to switch several similar functions
operator = {'a':processM, 'b':processSSI, 'c':processExcel, 'd':processWord}
operator.get(typeChoise)()

# This part is setting excel style...
def set_style():
	style = xlwt.XFStyle()
	font = xlwt.Font()
	font.name = 'Times New Roman'
	style.font = font	
	alignment = xlwt.Alignment()
	alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT
	style.alignment = alignment	
	return style

# This part is for write excel
f = xlwt.Workbook()
default = set_style()
sheet1 = f.add_sheet(u'subtestInfo', cell_overwrite_ok = True)
sheet1.col(0).width = 256 * 35
sheet1.write(0, 0, 'Worksheet for the Procedure: ', default)

# This part is for read excel
data = xlrd.open_workbook(f)
sourceExcel = data.sheets()[0]
nrows = sourceExcel.nrows
ncols = sourceExcel.ncols
sourceExcel.cell(i,j).value

# This part is for decorator
def decorate(func):
	cache = {}
	def wrap(n):
		if n not in cache:
			cache[n] = func(n)
		return cache[n]
	return wrap

@decorate
def fib2(n):
	if n == 1 or n == 0:
		return 1
	else:
		return fib2(n-1) + fib2(n-2)

# This part is for regular replace
re.sub('\d', 'e', '(1. xxx)\n(1. xxx)\n(1. xxx)\n(1. xxx)\n')

This part is for threading
def printIO(a):
	print a
	#time.sleep(1)
	print time.ctime()


threads = []
for i in range(4):
	t=Thread(target = printIO, args = [i])
	t.start()
	threads.append(t)

for t in threads:
	t.join()











































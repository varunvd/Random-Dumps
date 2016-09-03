#!/usr/bin/python
import os
code = { 'a':'!', 'h':'@', 'j':'#', 't':'$', 'l':'%', 'e':'/', 'f':'_', 'i':'-', 'b':'0', 'c':'1', 'd':'2', 'g':'3', 'p':'4', 'q':'5', 'r':'6', 's':'7', 'u':'8', 'o':'9', 'k':'a', 'm':'b' , 'n':'c', 'v':'d', 'w':'e', 'x':'f', 'y':'g', 'z':'h'}
num="0123456789"
lista="!@#$%/_\\-"
name=raw_input("Enter the file name\n")
data=open(name,'r')
d=''
for each_line in range(0,10000):
	str=data.readline()
	if str=='':
		break
	if str=='\n':
		continue
	for i in str:
		if i in num or i in lista:
			d=d+"|||"+i
			continue
		if i not in code and i not in num and i not in lista:
			d=d+i
			continue
		if i in code:
			d=d+code[i]
data.close()
data=open(name, 'w')
data.write(d)
data.close()



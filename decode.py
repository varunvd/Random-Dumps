#!/usr/bin/python
import os
e=''
counter=0
encode = { '!':'a', '@':'h', '#':'j', '$':'t', '%':'l', '/':'e', '_':'f', '-':'i', '0':'b', '1':'c', '2':'d', '3':'g', '4':'p', '5':'q', '6':'r', '7':'s', '8':'u', '9':'o', 'a':'k', 'b':'m' , 'c':'n', 'd':'v', 'e':'w', 'f':'x', 'g':'y', 'h':'z'}
name=raw_input("Enter the file to be decoded\n")
data=open(name, 'r')
for each_line in range(0,10000):
	d=data.readline()
	for i in range(0, len(d)):
		if d[i] not in encode and d[i]!='|':
			e=e+d[i]
			continue
		elif d[i]=='|' or d[i-1]=='|':
			counter=counter+1
			if counter==4:
				counter=0
				e=e+d[i]
			else:
				continue
			continue	
		elif d[i] in encode and d[i]!='|':
			e=e+encode[d[i]]
data.close()		
data=open(name,'w')
data.write(e)
data.close()
	
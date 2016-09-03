#!/usr/bin/python
str=raw_input("Enter a string\n")
str=str.replace(" ", "")
a=1
ans=[]
str1=str
for i in str:
	str=str[1:len(str)]
	if i not in str:
		str=str.replace(i,"")
	else:
		ans.append(i)
for i in str1:
	if i not in ans:
		print i

	

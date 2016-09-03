#!/usr/bin/python
n=int(raw_input("Enter the number"))
b=n*2-2
count=1
for i in range(1, n+1):
	print (b-count)*" "+count*"X "
	count=count+2
count=n+1
for i in range(1,n):
	print (b-count)*" "+count*"X "
	count=count-2


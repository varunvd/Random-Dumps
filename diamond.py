#!/usr/bin/python
n=int(raw_input("Enter the number\n"))
for i in range(1, n+1):
	print (n-i)*" "+i*"* "
for i in range(1,n):
	print i*" "+(n-i)*"* "

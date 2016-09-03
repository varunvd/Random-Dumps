#!/usr/bin/python
#This below line takes the number in the form of a string
a=raw_input("Enter the number\n")
#The below line selects all the numbers except the last digit
try:
	b=a[0:len(a)-1]
except:
	print 'unexpected input for the program'
#The below line selects last digit of the number
c=a[len(a)-1:len(a)]
#The line below performs the critical calculation
try:
	d=int(b)*int(c)+int(c)
except:
	print 'Unexcepted input for the program'
	exit()
print d

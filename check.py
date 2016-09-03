#!/usr/bin/python
N = int(raw_input("Enter the value of N"))
newans=[]
def isprime(a):
	for i in range(2, (a/2)+1):
		if a%i==0:
			print "False"
			return
	print "True"
def varun(n,N):
	for i in range(2, n+1):
		if n%i==0 and N%i==0:
			return False
	return True
for j in range(2, N):
	a=varun(j,N)
	if a==True:
		newans.append(j)
isprime(len(newans)+1)

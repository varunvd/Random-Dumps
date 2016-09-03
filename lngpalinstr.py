def palindrome(str)
	list=[]
	a=0

	result=""
	str=str.replace(" ", "")
	def add_substring(list, str, i):
		for j in range(0, len(str)-i):
			list.append(str[j:j+i+1])
	def palindrome(string):
		for i in range(0, len(string)/2):
			if string[i]!=string[-(i+1)]:
				return 0;
		return len(string)

	#This for loop creates all the substring
	for i in range(1, len(str)):
		add_substring(list,str,i)
	#This for loop checks if the string is a palindrome and also its length
	for string  in list:
		b=palindrome(string)
		if b!=0 and b>a:
			a=b
			result=string

	if result=="":
		print "No palindrome exists\n"
	else:
		print result

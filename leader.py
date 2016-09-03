a=int(raw_input("Enter the number of people in the country"))
name=[]
for i in range(0,a):
	name.append(raw_input())
check=[]
for i in range(0,a):
	v=name[i]
	v=set(v)
	check.append(len(v))
number=max(check)
for i in range(0,a):
	if number == int(check[i]):
		print name[i]
		break

from math import sin, cos, tan, pi
print "This intergration program works for dx function with expression having only one variable of x and does not work for trignometric functions"
a=float(raw_input("enter the lower limit\n"));
b=float(raw_input("enter the upper limit\n"));
expr=raw_input("Enter the expression\n");
def convert_to_pow(str):
	(b1,b2)=str.split('^',1)
	if b1[-1]!=')' and b2[0]!='(':
		count=-1
		c=''
		for i in range(0,len(b1)):
			if b1[count-i]=='+' or b1[count-i]=='-' or b1[count-i]=='*' or b1[count-i]=='/' or b1[count-i]=='^' or b1[count-i]=='(' or b1[count-i]==')':
				break;
			else:
				c=b1[count-i]+c
		d=''
		for i in range(0,len(b2)):
			if b2[i]=='+' or b2[i]=='-' or b2[i]=='*' or b2[i]=='/' or b2[i]=='^' or b2[i]=='w' or b2[i]=='(' or b2[i]==')':
				break;
			else:
				d=d+b2[i]
		b1=b1.__getslice__(0,len(b1)-len(c))
		b2=b2.__getslice__(len(d),len(b2))
		b=b1+"pow("+c+","+d+")"+b2
		return b
	if b1[-1]!=')' and b2[0]=='(':
		count=-1
		c=''
		for i in range(0,len(b1)):
			if b1[count-i]=='+' or b1[count-i]=='-' or b1[count-i]=='*' or b1[count-i]=='/' or b1[count-i]=='^' or b1[count-i]=='w' or b1[count-i]=='n':
				break;
			else:
				c=b1[count-i]+c
		d='('
		i=1
		level=1
		while(level!=0):
			if b2[i]=='(':
				level=level+1
			if b2[i]==')':
				level=level-1
			d=d+b2[i]
			i=i+1
		b1=b1.__getslice__(0,len(b1)-len(c))
		b2=b2.__getslice__(len(d),len(b2))
		b=b1+"pow("+c+","+d+")"+b2
		return b
	if b1[-1]==')' and b2[0]!='(':
		c=')'
		i=-2
		level=1
		while(level!=0):
			if b1[i]==')':
				level=level+1
			if b1[i]=='(':
				level=level-1
			c=b1[i]+c
			i=i-1
		d=''
		for i in range(0,len(b2)):
			if b2[i]=='+' or b2[i]=='-' or b2[i]=='*' or b2[i]=='/' or b2[i]=='s' or b2[i]=='p' or b2[i]=='w':
				break;
			else:
				d=d+b2[i]
		b1=b1.__getslice__(0,len(b1)-len(c))
		b2=b2.__getslice__(len(d),len(b2))
		b=b1+"pow("+c+","+d+")"+b2
		return b
	if b1[-1]==')' and b2[0]=='(':
		c=')'
		count=-1
		i=-2
		level=1
		while(level!=0):
			if b1[i]==')':
				level=level+1
			if b1[i]=='(':
				level=level-1
			c=b1[i]+c
			i=i-1
		d='('
		i=1
		level=1
		while(level!=0):
			if b2[i]=='(':
				level=level+1
			if b2[i]==')':
				level=level-1
			d=d+b2[i]
			i=i+1
		b1=b1.__getslice__(0,len(b1)-len(c))
		b2=b2.__getslice__(len(d),len(b2))
		b=b1+"pow("+c+","+d+")"+b2
		return b
for i in range(0, len(expr)-2):
	if '^' in expr:
		expr=convert_to_pow(expr)
count = 0
h=(b-a)/6
c=[]
d=[]
for b in range(0,7):
	c.append(a)
	a=a+h

for b in range(0,7):
	c[b]=str(c[b])
	d.append(expr.replace("x", c[b]))

for b in range(0,7):
	c[b]=eval(d[b])

ans=(3*h)/10
ans=ans*(c[0]+5*c[1]+c[2]+6*c[3]+c[4]+5*c[5]+c[6])
print ans

#!/usr/bin/env python
b=raw_input()
store_data=[]
convert = { '2':'a', '22':'b', '222':'c', '3':'d', '33':'e', '333':'f', '4':'g','44' : 'h', '444':'i', '5':'j', '55':'k', '555':'l', '6':'m', '66':'n', '666':'o', '7' : 'p', '77' : 'q', '777' : 'r' , '7777' : 's', '8' : 't', '88':'u', '888': 'v', '9': 'w', '99':'x', '999' : 'y', '9999':'z', '0' : ' ' }
def cut_it(a):
        count=0
        for i in range(1,len(a)):
                if a[i] != a[i-1]:
                        store_data.append(a[count:i])
                        count=i
        store_data.append(a[count:len(a)])
if __name__ == '__main__':
        b=b.split(' ')
        for i in b:
                cut_it(i)
        k=''
        for i in store_data:
                k=k+convert[i]
        print k

import pandas as pd
import xlrd

#This program will take the required data from the data sent from the placement cell and store it in the csv file

list = [ 2, 7, 8, 12, 13, 14, 15, 16, 17, 18, 19, 21, 44, 45, 46, 55, 56, 57 ]

mainlist = []

def store_values(a, result):
	re = []
	for i in list:
		try:
			re.append(str(a[i]))
		except:
			re.append(0)
	re.append(result)
	return re

filename = raw_input("Enter the file")
output = raw_input("Enter the csv file where it should be stored")

wb = xlrd.open_workbook(filename)
sh = wb.sheet_by_name('CSE')

for rownum in xrange(sh.nrows):
	a = sh.row_values(rownum)

	if a[4]=='' and a[5]=='':
		result = 0
	else:	
		result = 1
	
	re = store_values(a, result)
	
	mainlist.append(re)

apple = mainlist.pop(0)
apple[-1] = 'final_result'

df = pd.DataFrame(mainlist, columns = apple)
df.to_csv(output, sep=',')

print 'done'
	

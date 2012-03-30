#!/usr/bin/python
#from collections import defaultdict
import csv

cr = csv.reader(open('test.csv', 'rb'))
header = cr.next()
co = csv.writer(open('test2.csv','wb'))
for row in cr:
    if row[0][0] == 'sku':
        row = ''
    if row == row[0]:
        pass
    print row
    
def 
    try:
        index = row[2].index(' - ')
        if index > 0:
            # print row[2][0:index], 
            row[2] = row[2][0:index]
            print row[2]
    except:
        pass
    co.writerow(row)
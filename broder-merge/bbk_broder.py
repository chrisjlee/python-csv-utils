#!/usr/bin/env python
#from collections import defaultdict
import csv

"""
Merge the last three csv items and pipe them
@param row:
current row taken in from csv iterator
"""
def mergecat(row):
    return row[:-3] + ['|'.join(row[-3:])]
def decodePrices(row):
    return row[4].split(';')
cr = csv.reader(open('test.csv', 'rb'))
header = cr.next()
co = csv.writer(open('test2.csv','wb'))
for row in cr:
    if row == row[0]:
        pass
    try:
        index = row[2].index(' - ')
        if index > 0:
            # print row[2][0:index], 
            row.append(row[2][0:index])
            #print row[2]
    except:
        pass
    row = mergecat(row)
    print row
    if not row[0].startswith('SKU'):
      co.writerow(row)
#!/usr/bin/env python
import csv
import re
import os

"""
Clean the broder files and remove nasty characters
"""

with open("output.csv", "wt") as out:
    for l in open("update.csv", 'r'):
        l = l.replace('^', ',')
        # prices ([0-9]{2})(\.)([0-9]{2}) match = re.sub('([0-9]{2})(\.)([0-9]{2})','\0',l)
        #print l
        out.write(l)
def parse(fn, op):
    cr = csv.reader(open(fn, 'rb'))
    header = cr.next()
    co = csv.writer(open(op,'wb'))
    return cr, co
#"""
#  Replace seperated values
#      @param row: csv row
#      @param seperator: replaced text value to convert seperator 
#"""
#def seperate_values(row,seperator):
#    return row.replace(seperator,',')
## Return parsed values
cr, co = parse('output.csv','update2.csv')
header = cr.next()
for i, row in enumerate(cr):
    """
      Change the prices and remove the decimal
    """
    prices = row[18:23] #define the ranges 
    for id, price in enumerate(prices):
        prices[id] = price.replace('.','')
        row[18+id] = prices[id]
    co.writerow(row)
    #seperate_values(row,'^')
    
#def main():
#    return null
#if __name__ == '__main__':
#    main()
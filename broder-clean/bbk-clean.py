#!/usr/bin/env python
import csv
import re
import os

"""
Clean the broder files and remove nasty characters
"""

with open("output.csv", "wt") as out:
    for l in open("update.csv", 'r'):
        l = l.replace('^', ',', -1)
        print l
        out.write(l)
#def parse(fn, op):
#    cr = csv.reader(open(fn, 'rb'))
#    header = cr.next()
#    co = csv.writer(open(op,'wb'))
#    return cr, co
#"""
#  Replace seperated values
#      @param row: csv row
#      @param seperator: replaced text value to convert seperator 
#"""
#def seperate_values(row,seperator):
#    return row.replace(seperator,',')
## Return parsed values
###cr = parse('update.csv','output.csv')
#print co
#header = cr.next()
#
#for i, row in enumerate(cr):
#    print row
#    seperate_values(row,'^')
    
#def main():
#    return null
#if __name__ == '__main__':
#    main()
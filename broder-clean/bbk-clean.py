#!/usr/bin/env python
import csv
import os
import re
import sys
from itertools import izip

"""-------------------------------------------------------------------------
Clean the broder's csv file and remove nasty characters 
    and replaces it with commas
-------------------------------------------------------------------------"""
with open("output.csv", "wt") as out:
    for l in open("update.csv", 'r'):
        l = l.replace('^', ',')
        out.write(l)
"""-------------------------------------------------------------------------
Utility function that takes in a file

@param fn: 
    a string, takes in a path for the file being opened
@param op: 
    a string, takes in a path for the file being written to 
@return cr: 
    the csv reader object with read permissions
@return co: 
    the csv writer object with write permissions
-------------------------------------------------------------------------"""
def parse(fn, op):
    cr = csv.reader(open(fn, 'rb'))
    header = cr.next()
    co = csv.writer(open(op,'wb'))
    return cr, co
def merge_price_qty(prices):
    qty = ['0|1','2|12','13|-1']
    tmp = ["%s|%s" % (a,b) for a,b in zip(prices,qty)]
    return tmp
cr, co = parse('output.csv','update2.csv')
header = cr.next()
"""
Iterate through the csv
------------------------------------------------------
"""
for i, row in enumerate(cr):
    # Don't process the header duh
    if i == 0:
        header = row
        pass
    """
    Change the prices and remove the decimal
    ------------------------------------------------------
    """
    prices = row[18:23] # define the price cell ranges
    prices = [price.replace('.', '') for price in prices]
    prices = [int(price) for price in prices]
    prices = [price * 10 if price < 1000 else price for price in prices]
    """
    Merge Prices into price|qty|qty2;price|qty|qty2;price|qty|qty2 format
    ------------------------------------------------------
    """
    prices = merge_price_qty(prices)
    tmp = ';'.join(prices)
    newrow = row[:18] + [tmp] + row[23:]
    row = newrow
    """
    Add base url for broder
    ------------------------------------------------------
    """
    baseurl = 'http://www.broderbros.com/images/bro/prodDetail/'
    row[-3], row[-4] = baseurl + row[-3], baseurl + row[-4]
#    if row[1] == "NEW":
#        row =  row.append('new')
#        print row
    # Description
    desc = row[-2]
if __name__ == '__main__':
    """
    Write row to file
    ------------------------------------------------------
    """
    co.writerow(row)

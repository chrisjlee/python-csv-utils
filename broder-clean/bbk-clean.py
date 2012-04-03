#!/usr/bin/env python
import csv
import re
#import sys

#"""
#Clean the broder files and remove nasty characters
#---------------------------------------------------
#"""
with open("output.csv", "wt") as out:
    for l in open("update.csv", 'r'):
        l = l.replace('^', ',')
        out.write(l)

def parse(fn, op):
    cr = csv.reader(open(fn, 'rb'))
    header = cr.next()
    co = csv.writer(open(op,'wb'))
    return cr, co
# 
#def parse_images(images):
#    #print images
#    return row
cr, co = parse('output.csv','update2.csv')
header = cr.next()
for i, row in enumerate(cr):
    """
    Change the prices and remove the decimal
    ------------------------------------------------------
    """
    prices = row[18:23] # define the ranges
    prices = [price.replace('.', '') for price in prices]
    prices = [int(price) for price in prices]
    prices = [price * 10 if price < 1000 else price for price in prices]
    newrow = row[:18] + prices + row[23:]
    row = newrow
    print row
    # Images
    images = 'http://www.broderbros.com/images/bro/prodDetail/%s' % row[-3], 'http://www.broderbros.com/images/bro/prodDetail/%s' % row[-4]
    row[-3], row[-4] = images[0], images[1]
    # Description
    desc = row[-2]
    #print desc.replace('\xef\xbf\xbds','')
    co.writerow(row)
#def main():
#    
#if __name__ == '__main__':
#    main()
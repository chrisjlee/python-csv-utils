#!/usr/bin/env python
import csv, sys

def opencsv(fn, op):
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
    cr = csv.reader(open(fn, 'rb'))
    # header = cr.next()
    co = csv.writer(open(op,'wb'))
    return cr, co
if __name__ == '__main__':
    # Create a temporary list
    tmp = []
    # Grab the input / output path
    fn = sys.argv[1]
    fw = sys.argv[2]
    if (fn.find('.csv') > 0):
        cr, co = opencsv(fn,fw)
    for i, row in enumerate(cr):
        if i == 0:
            cat = 'Category'
            newrow = row[:-3]+ [cat]
            co.writerow(newrow)
            continue
        # Don't process the header
        tmp = row[-3:]
        tmp = '|'.join(row[-3:])
        newrow = row[:-3]+[tmp]
        co.writerow(newrow)
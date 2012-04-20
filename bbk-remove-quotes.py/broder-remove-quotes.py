#!/usr/bin/env python
import csv, sys, subprocess

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
    # Grab the input / output path
    fn = sys.argv[1]
    fw = sys.argv[2]
    if (fn.find('.csv') > 0):
        cr, co = opencsv(fn,fw)
    sub = subprocess.call(['sed', 's/^/,/g', fn, '>', fw])
    print sub
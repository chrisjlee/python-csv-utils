#!/usr/bin/env python
import csv
import os

"""
Clean the broder files and remove nasty characters
"""

class bbk: pass

def parse(fn, op):
    cr = csv.reader(open(fn, 'rb'))
    header = cr.next()
    co = csv.writer(open(op,'wb'))
    return cr, co
bbk.cr = parse('update.csv','output.csv')
for row in bbk.cr enumerate:
    print row
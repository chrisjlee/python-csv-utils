#!/usr/bin/python

import csv
import sys
import argparse

# parsing command line options
parser = argparse.ArgumentParser(prog='desc', description=__doc__)
parser.add_argument('-i', '--input', help='Input file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('-o', '--output', help='Output file', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
args = parser.parse_args(sys.argv[1:])
# Declare variables from input
inf, outf = args.input, args.output
outf = csv.writer(outf)

print 'Loading %s file into memory' % inf.name
data = []
tmp = 0.00
for i, line in enumerate(csv.reader(inf)):
    if i == 0:
        outf.writerow(line)
        continue
    #print line 
    price = "%.2f" % float(line[8])
    tmp = price.replace('.','')
    nl = line[:8] + [tmp] + line[10:]
    outf.writerow(nl)
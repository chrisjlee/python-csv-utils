#!/usr/bin/python
import csv
import sys
import argparse
import re

# creates a text file of all the colors in pipe seperated format
# parsing command line options
parser = argparse.ArgumentParser(prog='desc', description=__doc__)
parser.add_argument('-i', '--input', help='Input file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('-o', '--output', help='Output file', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
args = parser.parse_args(sys.argv[1:])
# Declare variables from input
inf, outf = args.input, args.output
#outf = csv.writer(outf)

print 'Loading %s file into memory' % inf.name
data = set()
results = []
lines = csv.reader(inf)
header = lines.next()
for row in lines:
    if not re.search('[^a-zA-Z\/\\\,\s]', row[5]):
        data.add(row[5].upper())
    else: continue
results = list(data)
output = ["%s|%s" %(i,i) for i in results]
for i in output:
    outf.write("%s\n" % i)
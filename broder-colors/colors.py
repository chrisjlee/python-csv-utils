#!/usr/bin/python
import csv
import sys
import argparse

# creates a text file of all the colors in pipe seperated format
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
needle = ''
for i, line in enumerate(csv.reader(inf)):
    if i == 0:
        continue
    needle = line[11]
    if len(data) == 0:
        data.append(needle)
        continue
    j = 0
    for j, item in enumerate(data):
        print item
        if needle == item:
            print 'match'
            continue
        else:
            print 'no match: appending item'
            data.append(item)
            continue
#!/usr/bin/python

import csv
import sys
import argparse

#parsing command line options
parser = argparse.ArgumentParser(prog='desc', description=__doc__)
parser.add_argument('-i', '--input', help='Input file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('-u', '--update', help='Update file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, required=True)
parser.add_argument('-o', '--output', help='Output file', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
args = parser.parse_args(sys.argv[1:])
inf, upf, outf = args.input, args.update, args.output
outf = csv.writer(outf)

print 'Loading %s file into memory' % inf.name
data = []
for i, line in enumerate(csv.reader(inf)):
	if i == 0:
		outf.writerow(line)
		continue

	p = line[3]
	p = p[:-1].split(';')
	p = [prices.split('|') for prices in p]
	prices = [p[0][0], p[1][0], p[2][0]]

	prices = ["%s.%s" % (split[:-2], split[-2:]) for split in prices]

	line[3] = "%s|0|1;%s|2|12;%s|13|-1;" % (prices[0], prices[1], prices[2])

	data.append(line)

print 'Loading %s file into memory' % upf.name
desc = []
for i, line in enumerate(csv.reader(upf)):
	if i == 0: continue
	desc.append(line)

print 'Processing %i lines on file %s, and %i lines on file %s' % (len(data), inf.name, len(desc), upf.name)
print '%i potential comparisons' % (len(data) * len(desc))
print 'Filling items with empty descriptions'
print

plines = set()
for i, line in enumerate(desc):
	#desc.append({line[1], line[3]})
	sku, description = line[1], line[3]

	for i, d in enumerate(data):
		skus = d[0]
		if sku in skus:
			new = d[:7] + [description] + d[8:]
			print 'Match! line #%i' % i
			data[i] = new
			plines.add(i)
			continue

print
print 'Writing data into file'

for line in data:
	outf.writerow(line)

print 'Done!'
print 'Lines not processed:'

diff = set()
for i in range(len(data)):
	diff.add(i)

print diff.difference(plines)

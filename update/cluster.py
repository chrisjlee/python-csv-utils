#!/usr/bin/python

import csv
import sys
import argparse

#parsing command line options
parser = argparse.ArgumentParser(prog='Cluster', description=__doc__)
parser.add_argument('-i', '--input', help='Input file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('-o', '--output', help='Output file', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
args = parser.parse_args(sys.argv[1:])
inputf, outputf = args.input, args.output
outputf = csv.writer(outputf)


title = ['']
prev = []

cats = set()
skus = set()

for i, line in enumerate(csv.reader(inputf)):
	if i == 0:
		outputf.writerow(line)
		continue

	exp = line[2].split('-')

	if (exp[0] != title[0]) and (i > 1):
		cluster = ['|'.join(skus)] + [prev[1]] + [' - '.join(title[:-2])]  + prev[3:-1] + ['|'.join(cats)]
		outputf.writerow(cluster)
		print cluster
		print
		cats.clear()
		skus.clear()

	cats.add(line[-1])
	skus.add(line[0])

	prev = line
	title = exp
else:
	cluster = ['|'.join(skus)] + [prev[1]] + [title[0]]  + prev[3:-1] + ['|'.join(cats)]
	outputf.writerow(cluster)
	cats.clear()
	skus.clear()

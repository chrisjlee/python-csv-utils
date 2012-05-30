#!/usr/bin/python

import csv
import sys
import argparse

#parsing command line options
parser = argparse.ArgumentParser(prog='Colors', description=__doc__)
parser.add_argument('-i', '--input', help='Input file', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
parser.add_argument('-o', '--output', help='Output file', nargs='?', type=argparse.FileType('w'), default=sys.stdout)
args = parser.parse_args(sys.argv[1:])
inputf, outputf = args.input, args.output
outputf = csv.writer(outputf)

for i, line in enumerate(csv.reader(inputf)):
	if i == 0:
		print [l for l in enumerate(line)]
		outputf.writerow(line)
		continue

	title = line[2].split(' - ')
	line[11] = title[-2]
	line[9] = title[-1]
	outputf.writerow(line)

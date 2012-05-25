#!/usr/bin/python

import csv
import sys
import argparse

#parsing command line options
parser = argparse.ArgumentParser(prog='Price Formatter ', description=__doc__)
parser.add_argument('-i', '--input', help='Input file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, required=True)
parser.add_argument('-u', '--update', help='Update file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, required=True)
parser.add_argument('-o', '--output', help='Output file', nargs='?', type=argparse.FileType('w'), default=sys.stdout, required=False)
args = parser.parse_args(sys.argv[1:])
i, u, o = args.input, args.update, args.output
o = csv.writer(o)

#print [i for i in enumerate(zip(csv.reader(i).next(), csv.reader(i).next()))]
#print
#print [i for i in enumerate(zip(csv.reader(u).next(), csv.reader(u).next()))]
#print
#exit()

#print 'Loading csv data into memory'
data = {}
column_number = 0

for i, line in enumerate(csv.reader(i)):
	n = len(line)
	if i == 0:
		o.writerow(line)
		column_number = n
		continue
	if n != column_number:
		line = line[0:2] + [line[2] + line[3]] + line[4:]
	new = line[0:1] + ['TRUE'] + line[2:5] + ['Broder'] + line[6:]
	data.update({line[0]:new})

#print 'Updating data'
for i, line in enumerate(csv.reader(u)):
	if i == 0:
		continue

	sku = line[1]

	# merge prices
	price = '%s|0|1;%s|2|12;%s|13|-1' % (line[4], line[5], line[6])
	image = line[16] + line[17]

	# attempt to find the same sku on csv data	
	try:
		old = data[sku]

		newline = [line[1], old[1], line[2], price, line[15], 'Broder', line[11], line[3], line[19], old[9], old[10], old[11], line[24], old[13], old[14], line[1], image, 'NEW']
		data[sku] = newline
	except KeyError:
		newline = [line[1], 'TRUE', line[2], price, line[15], 'Broder', line[11], line[3], line[19], '','','', line[24], '','', line[1], image, 'NEW']
		data.update({sku:newline})

#print 'Saving data onto disk'
for line in data:
	o.writerow(data[line])

#print 'done!'

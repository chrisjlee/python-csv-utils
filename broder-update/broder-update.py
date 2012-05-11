#!/usr/bin/env python
# This snippet demonstrates how to read a CSV file into a dictionary of
# dictionaries in order to be able to query it easily.
# The full documentation for the csv module is available here:
# http://docs.python.org/library/csv.html
#
# First things first, we need to import the csv module
# Also import sys to get argv[0], which holds the name of the script
#
import csv
import sys
import itertools
import argparse

# Derive the name of the CSV file from the name of the script and initialise
# the headers list and content dictionary
def parse_arguments():
    """
    Function manages arguments
    """
    parser = argparse.ArgumentParser(prog='Price Formatter ', description=__doc__, epilog='Author: Chris Lee (chris@globerunnerseo.com)')
    parser.add_argument('-i', '--input', help='Input file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, required=True)
    parser.add_argument('-u', '--update', help='Update file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, required=True)
    parser.add_argument('-o', '--output', help='Output file', nargs='?', type=argparse.FileType('w'), default=sys.stdout, required=False)
    # Take everything except the file name and store them into `args`
    args = parser.parse_args(sys.argv[1:])
    # Convert each arg into the `argsdict` dictionary 
    argsdict = vars(args)
    # Return each argument 
    return argsdict['input'], argsdict['update'], argsdict['output']
def csv_to_dict(file):
    d = csv.DictReader(file, dialect='excel', delimiter=',')
    #for row in d:
        #for key in row:
            # d = key, row[key]
            # print 'key=%s, value=%s' % (key, row[key])
            # print d[key]
    return d
#reader=csv.reader(open(fi))
#for row in reader:
#    if reader.line_num == 1:
#        """
#        If we are on the first line, create the headers list from the first row
#        by taking a slice from item 1  as we don't need the very first header.
#        """
#        headers = row[1:]
#    else:
#        """
#        Otherwise, the key in the content dictionary is the first item in the
#        row and we can create the sub-dictionary by using the zip() function.
#        We also know that the stabling entry is a comma separated list of names
#        so we split it into a list for easier processing.
#        """
#        content[row[0]] = dict(zip(headers, row[1:]))
#        content[row[0]]['Stabling'] = [s.strip() for s in content[row[0]]['Stabling'].split(',')]
#
## We can know get to the content by using the resulting dictionary, so to see
## the list of lines, we can do:
#print "\nList of lines"
#print content.keys()
## To see the list of statistics available for each line
#print "\nAvailable statistics for each line"
#print headers
#
#header = ["SKU","Status","Title","Price","Weight","Company","Style Code","Features","Retail Price","Size","Hex Color","Color","Mill Name","Dimensions","Imprint Area","Item Number","Image","Category"]
#
#
def csv_to_dict(file):
    return csv.DictReader(file, dialect='excel', delimiter=',')
"""
    main function
-------------------------------------------------------------------------"""
if __name__ == '__main__':
    # Grab the input / output path
    input, update, output = parse_arguments()
    args = [input, update] 
    d = csv_to_dict(input)
    u = csv_to_dict(update)
    allrows = list(csv.reader(update))
    # Extract the first row as keys for a columns dictionary
    cols = dict([(x[0],x[1:]) for x in zip(*allrows)])
    print cols
#    for key in d:
#        print l['NEW']
#        if l['NEW'] == 'NEW': 
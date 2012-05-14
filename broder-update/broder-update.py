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

#
# Usage Example: ./broder-update.py -u  update.csv -i broder-entities.csv -o output.csv
#

# Derive the name of the CSV file from the name of the script and initialise
# the headers list and content dictionary
def parse_arguments():
    """ Function manages arguments """
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
#def print_header(dh,Dy):
#    for i,z in (zip (dh,Dy)):
#        print 'input: %s \t update: %s' % (i,z)
def csv_to_dict(file):
    """ take the file (csv reader) """
    return csv.DictReader(file, dialect='excel', delimiter=',')
""" main function
-------------------------------------------------------------------------"""
if __name__ == '__main__':
    import doctest
    
    # Create a list for matching header columns
    mc = [] 
    # Grab the input / output path
    input, update, output = parse_arguments()
    # create a dictionary object from the input
    d = csv_to_dict(input)
    # create a dict from an  update file
    u = csv_to_dict(update)
    #d = csv.DictReader(input, dialect='excel', delimiter=',') #csv_to_dict(input)
    #u = csv.DictReader(update, dialect='excel', delimiter=',') # csv_to_dict(update)
    dh = [f for f in d.fieldnames]
    uh = [f for f in u.fieldnames]
    """ """
    matches = []
    # Take one list and loop through it
    for i in dh:
        # Now loop through the other list - the second list should be shorter
        # @todo: detect which list is the shorter one
        for k in uh:
            # Compare
            if k.lower() == i.lower():
                matches.append(k)
    print matches
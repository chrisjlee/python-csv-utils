#!/usr/bin/env python
import csv
import sys
import itertools
import argparse

"""
Project Overview:
- Script merges two files
-- `broder-entities` file contains the current data
-- `update.csv` contains new 2012 pricing
- Lookup sku in update if it doesn't exist in broder-entities.csv add a category "New", append to end
- Otherwise merge common fields: price, retail price, etc

"""


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
def csv_to_dict(file):
    """ take the file (csv reader) and return dict object """
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
    # find the headings for each dictionary object
    dh = [f for f in d.fieldnames]
    uh = [f for f in u.fieldnames]
    # Create a empty list for matching columns
    matches = []
    # Attempting to find matching columns of csv
    # Take one list and loop through it
    for i in dh:
        # Now loop through the other list - the second list should be shorter
        # @todo: detect which list is the shorter one
        for k in uh:
            # Compare titles and strip the text from both sides
            if k.lower().strip() == i.lower().strip():
                matches.append(k)
    line = []
    # @todo find matching columns and merge
    for k in d: 
        for i in matches:
            line.append(k[i])
            print line
            # if i == len(matches):
            break
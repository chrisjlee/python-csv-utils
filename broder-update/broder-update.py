#!/usr/bin/env python
import csv, argparse, sys
header = ["SKU","Status","Title","Price","Weight","Company","Style Code","Features","Retail Price","Size","Hex Color","Color","Mill Name","Dimensions","Imprint Area","Item Number","Image","Category"]

def parse_arguments():
    """
    Function manages arguments
    """
    parser = argparse.ArgumentParser(prog='Price Formatter ', description=__doc__, epilog='Author: Chris Lee (chris@globerunnerseo.com)')
    parser.add_argument('-i', '--input', help='Input file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, required=True)
    parser.add_argument('-u', '--update', help='Update file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, required=True)
    parser.add_argument('-o', '--output', help='Output file', nargs='?', type=argparse.FileType('w'), default=sys.stdout, required=False)
    args = parser.parse_args(sys.argv[1:])
    argsdict = vars(args)
    return argsdict['input'], argsdict['update'], argsdict['output']
def validate_header():
    print 'yay'
def open_csv(fn, op):
    """-------------------------------------------------------------------------
    Utility function that takes in a file
    
    @param fn: 
        a string, takes in a path for the file being opened
    @param op: 
        a string, takes in a path for the file being written to 
    @return cr: 
        the csv reader object with read permissions
    @return co: 
        the csv writer object with write permissions
    -------------------------------------------------------------------------"""
    cr = csv.reader(open(fn, 'rb'))
    # header = cr.next()
    co = csv.writer(open(op,'wb'))
    return cr, co
"""
    main function
-------------------------------------------------------------------------"""
if __name__ == '__main__':
    # Grab the input / output path
    input, output = parse_arguments()
    cr, co = open_csv(input)
    with cr as f:
        f.readline() # ignore first line (header)
        mydict = dict(csv.reader(f, delimiter=','))
    print mydict
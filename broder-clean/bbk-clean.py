#!/usr/bin/env python
import csv, re, sys, argparse, tempfile, shutil
import tempfile, shutil, os
"""
Reads through a highly formatted csv file and reorganizes the
pricing. Written with BBK's csv format in mind.

Broder Input CSV Format:
    ['Category Page Number', 'NEW', 'SKU', 'Style', 'Short Description', 'Color Group', 'Color Code', 'Color', 'Hex Code', 
    'Size Group', 'Size Code', 'Size', 'Case Qty', 'Weight', 'Mill #', 'Mill Name', 'Category', 'Subcategory', 'P1 (Piece)', 'P2 (Dozen)', 
    'P4 (Case)', 'P7 (Preferred)', 'Retail Price', 'Thumbnail Name', 'Normal Image Name', 'Full Feature Description', 'Brand Page Number']
"""

def __var():
    """-------------------------------------------------------------------------
        static __var()
        provides a configuration variable to instantiate configuration variables
    -------------------------------------------------------------------------"""
    h, l = []
    baseurl = ''
    return h,l,baseurl
def parse(fn, op):
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
def merge_price_qty(prices):
    """-------------------------------------------------------------------------
    Merge Price and quantity into table list formats
        `price|qty|qty2;price|qty|qty2;price|qty|qty2`
    -------------------------------------------------------------------------"""
    # set quantity
    qty = ['0|1','2|12','13|-1']
    tmp = ["%s|%s" % (a,b) for a,b in zip(prices,qty)]
    return tmp
def create_temporary_copy(path):
    temp_dir = tempfile.gettempdir()
    temp_path = os.path.join(temp_dir, 'temp_file_name')
    shutil.copy2(path, temp_path)
    return temp_path
def parse_arguments():
    """
    Function manages arguments
    """
    parser = argparse.ArgumentParser(prog='Price Formatter ', description=__doc__, epilog='Author: Chris Lee (chris@globerunnerseo.com)')
    parser.add_argument('-i', '--input', help='Input file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, required=True)
    parser.add_argument('-o', '--output', help='Output file', nargs='?', type=argparse.FileType('w'), default=sys.stdout, required=True)
    args = parser.parse_args(sys.argv[1:])
    argsdict = vars(args)
    return argsdict['input'], argsdict['output']
"""
    main function
-------------------------------------------------------------------------"""
if __name__ == '__main__':
    # Grab the input / output path
    fi, fo = parse_arguments()
    # Create storage for temporary list for lines
    lines = []
    # create tmp list variable 
    tmp = []
    # define what the baseurl is
    baseurl = 'http://www.broderbros.com/images/bro/prodDetail/'
    
    """
    Clean the broder's csv file and remove nasty characters 
    and replaces it with commas
    -------------------------------------------------------------------------"""
    for l in fi:
        l = l.replace('^', ',')
        fo.write(l)
    # cr, co = parse('output.csv','update2.csv')

    o = open("output.csv", "wt")
    with o as out:
        for l in open("update.csv", 'r'):
            l = l.replace('^', ',')
            out.write(l)
        cr, co = parse('output.csv','update2.csv')
    o.close()
    print h[0]
    l.append(tmp)
    """
    Iterate through the csv
    --------------------------------------------------------------"""
#    for i, row in enumerate(cr):
#        # Don't process the header
#        if row[0] == 'Category Page Number':
#            # new row = everything up to price + price table + everything else afterwards 
#            newrow = row[:18] + ['Price'] + row[22:]
#            lines.append(newrow)
#            continue
#        """
#        Change the prices and remove the decimal
#        --------------------------------------------------------------"""
#        prices = row[18:23] # define the price cell ranges
#        prices = [price.replace('.', '') for price in prices]
#        prices = [int(price) for price in prices]
#        prices = [price * 10 if price < 1000 else price for price in prices]
#        retail = prices[4]
#        """
#        Merge Prices into price|qty|qty2;price|qty|qty2;price|qty|qty2 format
#        --------------------------------------------------------------"""
#        prices = merge_price_qty(prices)
#        tmp = ';'.join(prices)
#        newrow = row[:18] + [tmp] + [retail] + row[23:] 
#        row = newrow
#        """
#        Add base url for broder
#        --------------------------------------------------------------"""
#        row[-3], row[-4] = baseurl + row[-3], baseurl + row[-4]
#        desc = row[-2]
#        """
#        Write row to file
#        ------------------------------------------------------
#        """
#        lines.append(row)
#    for line in lines:
#        co.writerow(line)
#!/usr/bin/env python
import csv
import argparse
import sys
import os

"""
Example usage: ./bbk-clean.py -i Broder-AllDBInfoBRO.csv -o output.csv

-i    --input  Takes in a file
-o    --output File that it will output to

Reads through a highly formatted csv file and reorganizes the
pricing. Written with BBK's csv format in mind.

Broder Input CSV Format:
['Category Page Number', 'NEW', 'SKU', 'Style', 'Short Description', 'Color Group', 'Color Code', 'Color', 'Hex Code', 
'Size Group', 'Size Code', 'Size', 'Case Qty', 'Weight', 'Mill #', 'Mill Name', 'Category', 'Subcategory', 'P1 (Piece)', 'P2 (Dozen)', 
'P4 (Case)', 'P7 (Preferred)', 'Retail Price', 'Thumbnail Name', 'Normal Image Name', 'Full Feature Description', 'Brand Page Number']
"""
def merge_price_qty(prices):
    """-------------------------------------------------------------------------
    Merge Price and quantity into table list formats
        `price|qty|qty2;price|qty|qty2;price|qty|qty2`
        @param prices:
        takes in a list of prices
        @returns tmp, a list of prices
    -------------------------------------------------------------------------"""
    # set quantity
    qty = ['0|1','2|12','13|-1']
    tmp = ["%s|%s" % (a,b) for a,b in zip(prices,qty)]
    return tmp
def parse_arguments():
    """
    Function manages arguments
    """
    parser = argparse.ArgumentParser(prog='Price Formatter ', description=__doc__, epilog='Author: Chris Lee (chris@globerunnerseo.com)')
    parser.add_argument('-i', '--input', help='Input file', nargs='?', type=argparse.FileType('r'), default=sys.stdin, required=True)
    parser.add_argument('-o', '--output', help='Output file', nargs='?', type=argparse.FileType('w'), default=sys.stdout, required=False)
    args = parser.parse_args(sys.argv[1:])
    argsdict = vars(args)
    return argsdict['input'], argsdict['output']
"""
    main function
-------------------------------------------------------------------------"""
if __name__ == '__main__':
    # Grab the input / output path
    fi, fo = parse_arguments()
    # tp = create_temporary_copy(fi.name)
    # Create storage for temporary list for lines
    lines = []
    # create tmp list variable
    tmp = []
    # define what the baseurl is
    baseurl = 'http://www.broderbros.com/images/bro/prodDetail/'
    cr = csv.reader(fi, delimiter='^')
    co = csv.writer(fo, delimiter=',')
    """
    Iterate through the csv
    --------------------------------------------------------------"""
    for i, row in enumerate(cr):
        # Don't process the header
        if row[0] == 'Category Page Number':
            # new row = everything up to price + price table + everything else afterwards 
            newrow = row[:18] + ['Price'] + row[22:]
            lines.append(newrow)
            continue
        """
        Change the prices and remove the decimal
        --------------------------------------------------------------"""
        prices = row[18:23] # define the price cell ranges Price range should include retail price
        prices = [price.replace('.', '') for price in prices]
        prices = [int(price) for price in prices]
        prices = [price * 10 if price < 1000 else price for price in prices]
        retail = prices[4]
        """
        Merge Prices into price|qty|qty2;price|qty|qty2;price|qty|qty2 format
        ---------------------------------------------------------------"""
        prices = merge_price_qty(prices)
        tmp = ';'.join(prices)
        newrow = row[:18] + [tmp] + [retail] + row[23:] 
        row = newrow
        """
        Add base url for broder
        --------------------------------------------------------------"""
        row[-3], row[-4] = baseurl + row[-3], baseurl + row[-4]
        desc = row[-2]
        # aggregate and write rows to `lines` variable buffer
        lines.append(row)
    for line in lines:
        co.writerow(line)
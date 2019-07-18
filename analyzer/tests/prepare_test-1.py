#!/usr/bin/env python3

import re
import csv

def main(fn):
    with open(fn) as f:
        reader = csv.reader(f, dialect='excel-tab')
        for base, infl, prop in reader:
            prop=prop.replace(' ', '+')
            infl = infl.strip()
            print(f'{infl}\t{base}{prop}')

if __name__ == '__main__':
    main('test_set-1.tsv')

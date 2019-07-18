#!/usr/bin/env python3

import sys
import csv
from Levenshtein import distance

def analyses_to_set(analyses):
    analyses = analyses.split('\n')
    return {x.split('\t')[1].replace('+Guess', '') for x in analyses}

def main(test_fn, gold_fn):
    with open(test_fn) as test_f:
        test = test_f.read()
        test = test.split('\n\n')
    with open(gold_fn) as gold_f:
        gold = [x.strip() for x in gold_f]
    for g, t in zip(gold, test):
        ans = analyses_to_set(t)
        if g in ans:
            print('Success:', g, ans)
        else:
            print('Failure:', g, ans)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

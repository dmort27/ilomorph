#!/usr/bin/env python3

from nltk.corpus import wordnet
import csv
import sys
import re

WHITESPACE = re.compile('\s')

def main(input_fn, nouns_fn, other_fn):
    with open(input_fn, encoding='utf-8') as input_f:
        reader = csv.reader(input_f, dialect='excel-tab')
        with open(nouns_fn, 'w', encoding='utf-8') as nouns_f, open(other_fn, 'w', encoding='utf-8') as other_f:
            for eng, ilo in reader:
                if WHITESPACE.search(ilo): continue
                if all([s.pos() == 'n' for s in wordnet.synsets(eng)]):
                    print('{} Enclitic; ! {}'.format(ilo, eng), file=nouns_f)
                else:
                    print('{} Enclitic; ! {}'.format(ilo, eng), file=other_f)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])

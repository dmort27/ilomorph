import re

# Define regular expressions for consonants and vowels
C = 'p|t|k|b|d|g|ts|ti|di|s|si|h|m|n|ni|ng|l|li|r|rr|w|y'
V = 'a|e|i|o|u'

# Compile regular expressions to match reduplication patterns
CVC = re.compile('(?P<red>(?:{}|)(?:{})(?:{}))-?(?P=red)'.format(C, V, C))
CV  = re.compile('(?P<red>(?:{}|)(?:{}))-?(?P=red)'.format(C, V))

# Encode lexical exceptions
EXCEPTIONAL = dict([
    ('babbaket', '<RED>baket'),
    ('babbalasang', '<RED>balasang'),
    ('babbalo', '<RED>balo'),
    ('babbaro', '<RED>baro'),
    ('lallakay', '<RED>lakay'),
    ('tattao', '<RED>tao'),
    ('addi', '<RED>adi'),
    ('amma', '<RED>ama'),
    ('annak', '<RED>anak'),
    ('appo', '<RED>apo'),
    ('assawa', '<RED>asawa'),
    ('babbai', '<RED>babai'),
    ('inna', '<RED>ina'),
    ('ingnga', '<RED>inga'),
    ('lallaki', '<RED>lalaki'),
    ('ubbing', '<RED>ubing'),
])

def dedup(token):
    # If the token is in the list of exceptions, output the listed value
    if token in EXCEPTIONAL:
        return EXCEPTIONAL[token]
    # If the token matches a CVC reduplication pattern, apply this substitution
    elif CVC.match(token):
        return CVC.sub(r'<RED>\g<red>', token)
    # Otherwise, try a CV reduplication pattern
    else:
        return CV.sub(r'<RED>\g<red>', token)

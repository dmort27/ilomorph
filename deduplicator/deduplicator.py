import re

C = 'p|t|k|b|d|g|ts|ti|di|s|si|h|m|n|ni|ng|l|li|r|rr|w|y'
V = 'a|e|i|o|u'

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

CVC = re.compile('(?P<red>(?:{}|)(?:{})(?:{}))-?(?P=red)'.format(C, V, C))
CV  = re.compile('(?P<red>(?:{}|)(?:{}))-?(?P=red)'.format(C, V))

def dedup(token):
    if token in EXCEPTIONAL:
        return EXCEPTIONAL[token]
    elif CVC.match(token):
        return CVC.sub(r'<RED>\g<red>', token)
    else:
        return CV.sub(r'<RED>\g<red>', token)

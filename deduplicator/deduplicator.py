import re

C = 'p|t|k|b|d|g|ts|ti|di|s|si|h|m|n|ni|ng|l|li|r|rr|w|y'
V = 'a|e|i|o|u'

CVC = re.compile('(?P<red>(?:{}|)(?:{})(?:{}))-?(?P=red)'.format(C, V, C))
CV  = re.compile('(?P<red>(?:{}|)(?:{}))-?(?P=red)'.format(C, V))

def dedup(token):
    def red2morph(m):
        return '<RED>' + m.group('red')
    if CVC.match(token):
        return CVC.sub(r'<RED>\g<red>', token)
    else:
        return CV.sub(r'<RED>\g<red>', token)

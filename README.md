IloMorph
========

IlmoMorph is a morphological analyzer for Ilocano. Usage:

```python
>>> from ilomorph import IloMorph

>>> m = IloMorph('ilo.fst')
>>> m.lemmas(['nakitadakami', 'babbaket'])
['nakita', 'baket']
>>> m.analyses(['nakitadakami', 'babbaket'])
[['nakita', 'Guess', '2Erg', 'PlErg', '1Abs', 'PlAbs', 'ExclAbs'], ['baket', 'Guess']]
```

You must have three files:
* `fstinter.py` -- Interface for flookup
* `ilomorph.py` -- Python interface to the FST
* `ilo.fst` -- The FST

You must also have Foma installed (`flookup` needs to be in your path).

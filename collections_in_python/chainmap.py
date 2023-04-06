#chainmap is use to make a single view of multiple dictionary

from collections import ChainMap

a = {'name': 'emmy', 'language': 'python'}
b = {'program1': 'ML', 'program2': 'AI'}

s = ChainMap(a,b)
print(s)


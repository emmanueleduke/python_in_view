#ordered dict is a dictionary subclass which remembers the order in which the entries were done
#if the key is changed, the position of the value will not be changed
from collections import OrderedDict
d = OrderedDict()
d[1]='e'
d[2]='d'
d[3]='u'
d[4]='k'
d[5]='e'
print(d)

#return the keys and values
print(d.keys())
print(d.items())

#to change a character
d[1]='p'
print(d)

#defaultdict is a dictionary subclass which calls a factory function a supply a missing value
from collections import defaultdict

#specify the class
d = defaultdict(int)

d[1]='python'
d[2]='language'
print(d)

#when a key called is not define, no error is return
print(d[3])

#observe the difference with the usual dictionary that return error message 

dic = {1:'a', 2:'b'}
print(dic[3])

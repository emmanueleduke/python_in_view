#Counter() is a dictionary subclass for counting hashable objects...

from collections import Counter

a = [1,1,2,3,2,2,4,5,4,5,4,3,6,2,2]
b = Counter(a)
print(b)

#to return the a list of the values orderly

print(list(b.elements()))

#using most_common()

print(b.most_common())

#subtract()

sub = {2:1, 5:1}
print(b.subtract(sub))
print(b.most_common())

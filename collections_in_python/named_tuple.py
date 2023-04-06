from collections import namedtuple
a = namedtuple('course', 'program, technology')
#b =a('software engineering', 'python')
b = a._make(['AI', 'python'])
print(b)

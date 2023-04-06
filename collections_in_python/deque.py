#deque() is use in insertion and deletion

from collections import deque

a = ['e', 'd', 'u', 'k', 'e']
b = deque(a)
print(b)

#to insert a character or string to the list!
b.append('python')
print(b)

#to insert at the beginning

b.appendleft('python')
print(b)

#to delete from the end

b.pop()
print(b)

#to delete from the beginning
b.popleft()
print(b)


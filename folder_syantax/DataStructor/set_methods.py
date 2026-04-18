s={34,23,1,3,22}
print(s)

s.add(32)
print(s)

s.remove(23)
print(s)

# remove only work if the element is present if not present through an erreor
'''
s.remove(345665)
print(s)
'''


# Discard()
s.discard(345665)
print(s)


# pop()
'''
s.pop(2)
print(s)
'''
# set concepts union intersection
a={1,2,3,4,3}
b={7,8,9,3,4}

d=a.union(b)
print(d)

e=a.intersection(b)
print(e)
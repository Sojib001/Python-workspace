s = {1, 0 , -1 , 2, 3, 5, -2, -3 , -4}
print(len(s))
print(s)
s.add(100)
print(s)
s.remove(100) # using discard is better
# if not found in the set, remove will throw an error
print(s)

# s1 = {1, 2, 3}
# s2 = {2, 3, 4}
# print(s1.union(s2))
# s1.update(s2)
# print(s1)
# print(s1.intersection(s2))
# s1.difference_update(s2)
# print(s1.difference(s2))
# print(s1)

# difference
# difference_update
# intersection
# intersection_update
# iddisjoint
# issuperset
# issubset
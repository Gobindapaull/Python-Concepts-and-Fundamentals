s = set()
print(type(s))

s.add(1)
s.add(2)
s.add(2)

print(s)

s1 = {3, 4, 5, 6}
s2 = {5, 6, 7, 8}

print(s1 | s2) # join both set
# 3, 4, 5, 6, 7, 8

print(s1 & s2) # common in both set
# 5, 6

print(s1 - s2) # only available in s1
# 3, 4

print(s1 ^ s2)
# 3, 4, 7, 8

list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
s3 = set(list)
print(s3) # remove duplicate element

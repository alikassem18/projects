# From decimal to binary.

a = '14'
# 1110

b = [int(x) for x in a]
print(b)

c = 1
d = []
while c <= int(a):
    d.insert(0, c)
    c = c*2
print(d)

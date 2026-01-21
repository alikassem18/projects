# From binary to decimal (optimized version).

a = input('Enter a binary number:')
print(a)


b = [int(x) for x in a]
print(b)


c = [(2**y) for y in range(len(b))]
c.reverse()
print(c)

d = 0
for z in range(1, len(c)+1):
    if b[-z] == 1:
        d = d + c[-z]

print(d)

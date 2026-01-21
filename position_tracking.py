# Motion of a point in 2D.

x = 'up 4 right 6 up 2 left 8 down 5 down 3 left 1 up 6 right 5 down 5'
y = x.split(' ')
a = 0
b = 0
c = 0
d = 0
for z in range(len(y)):
    if  y[z] == 'right':
        a = a + int(y[z+1])
    if  y[z] == 'left':
        b = b + int(y[z+1])
    if y[z] == 'up':
        c = c + int(y[z+1])
    if y[z] == 'down':
        d = d + int(y[z+1])

X = a-b
Y = c-d

print(f'({X},{Y})')
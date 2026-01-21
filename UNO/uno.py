import random

from utils import maincards, fett, kabber, es7ab

p = {'me': [], 'pc': [[],[]]}
table = []
cards = []
co = 'RBYG'
ch = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'S', 'D2', 'R', 'D4', 'W']

for x in co:
  for y in ch[:-2]:
    z = x+y
    cards.append(z)
cards.extend(cards)

for x in co:
  cards.append(x+'0')
  cards.extend(ch[-2:])
  
random.shuffle(cards)

###############################################################################################################################################

yfett = kabber(cards)

maincards(cards, p[yfett])

fett(cards, 'me', p['me'], p['pc'][0], table)

print(table[-1])

for tt in range(10):
  x = table[-1]
  for z in p['pc'][0]:
    if z[0] == x[0] or z[1] == x[1]:
      p['pc'][1].append(z)
      p['pc'][0].remove(z)
  if len(p['pc'][1]) != 0:
    table.append(random.choice(p['pc'][1]))
    print(len(p['pc'][0]))
    print(table[-1])
  else:
    es7ab(cards, p['pc'][0])
    print(len(p['pc'][0]))
    print('PC:sa7abet')

  print(p['me'])
  print(table[-1])
  myturn = input("it's your turn:")
  if myturn == 'sa7abet':
    es7ab(cards, p['me'])
  else:
    table.append(myturn)
    p['me'].remove(myturn)
    print(table[-1])

  '''if len(p['pc'][0]) == 1 or len(p['me']) == 1:
    print('uno!')'''
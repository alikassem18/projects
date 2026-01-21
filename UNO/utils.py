import random

def o2ta3(cards, yo2ta3 = None):
  cardindex = random.randint(1,len(cards))
  m2tou3 = cards[0:cardindex]
  if m2tou3[-1] == 'D4':
    print('Plus Four!')
    if yo2ta3 is not None:
      yo2ta3.append(m2tou3[-1])
      m2tou3.remove(m2tou3[-1])
  return (m2tou3, cardindex)
###############################################################################################################################################
def kabber(cards):
  while True:
    X = o2ta3(cards)
    Y = o2ta3(cards)
    x = X[0]
    y = Y[0]
    if x[-1] != y[-1]:
      o = max(x, y)
      if o == x:
        return 'me'
      elif o == y:
        return 'pc'

def maincards(cards, yo2ta3):
  m2tou3, cardindex = o2ta3(cards, yo2ta3)
  be2e = cards[cardindex:]
  cards.clear()
  cards.extend(be2e + m2tou3)

def fett(cards, yfett, me, pc, table):
  if yfett == 'pc':
    me.append(cards[0])
    pc.append(cards[1])
  elif yfett == 'me':
    pc.append(cards[0])
    me.append(cards[1])
  cards.remove(cards[0])
  cards.remove(cards[0])
  while len(me) != 7 or len(pc) != 7:
    if yfett == 'pc':
      me.extend(cards[:2])
      pc.extend(cards[2:4])
    elif yfett == 'me':
      pc.extend(cards[:2])
      me.extend(cards[2:4])
    cards.remove(cards[0])
    cards.remove(cards[0])
    cards.remove(cards[0])
    cards.remove(cards[0])
  table.append(cards[0])
  cards.remove(cards[0])

def es7ab(cards, p, nb = 1):
  p.extend(cards[:nb])
  for x in range(nb):
    cards.remove(cards[0])


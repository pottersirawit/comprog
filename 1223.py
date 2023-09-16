class Card:
 def __init__(self, value, suit):
     self.value = value
     self.suit = suit
 def __str__(self):
     return '('+self.value+' '+self.suit+')'
 def next1(self):
    l = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
    ln = ['club','diamond','heart','spade']
    return Card(l[((ln.index(self.suit)+1)//4+l.index(self.value))%13],ln[(ln.index(self.suit)+1)%4])
 def next2(self):
    l = ['3','4','5','6','7','8','9','10','J','Q','K','A','2']
    ln = ['club','diamond','heart','spade']
    self.value=l[((ln.index(self.suit)+1)//4+l.index(self.value))%13]
    self.suit=ln[(ln.index(self.suit)+1)%4]
n = int(input())
cards = []
for i in range(n):
 value, suit = input().split()
 cards.append(Card(value, suit))
for i in range(n):
 print(cards[i].next1())
print("----------")
for i in range(n):
 print(cards[i])
print("----------")
for i in range(n):
 cards[i].next2()
 cards[i].next2()
 print(cards[i])

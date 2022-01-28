import random

suites = ( 'Hearts', 'Diamonds', 'Spades', 'Clubs')
card_names = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card():
  def __init__(self, suite, value):
    self.suite = suite
    self.value = value

class Deck:
  def __init__(self):
    self.suites = ( 'Hearts', 'Diamonds', 'Spades', 'Clubs')
    self.card_names = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
    self.deck = []


  def build(self):
    for s in self.suites:
      for card in self.card_names:
        self.deck.append(Card(s,card))

  def get_deck(self):
    return self.deck


## Neeeds to return string values.  Working. 

d = Deck()
d.build()
print(d.get_deck())
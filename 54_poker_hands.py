#!/usr/bin/python

# In the card game poker, a hand consists of five cards and are ranked, from
# lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest
# value wins; for example, a pair of eights beats a pair of fives (see example 1
# below). But if two ranks tie, for example, both players have a pair of queens,
# then highest cards in each hand are compared (see example 4 below); if the
# highest cards tie then the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:

# 1 5H 5C 6S 7S KD
# Pair of Fives
# 2C 3S 8S 8D TD
# Pair of Eights
# Winner Player 2

# 2 5D 8C 9S JS AC
# Highest card Ace
# 2C 5C 7D 8S QH
# Highest card Queen
# Winner Player 1

# 3 2D 9C AS AH AC
# Three Aces
# 3D 6D 7D TD QD
# Flush with Diamonds
# Winner Player 2

# 4 4D 6S 9H QH QC
# Pair of Queens
# Highest card Nine
# 3D 6D 7H QD QS
# Pair of Queens
# Highest card Seven
# Winner Player 1

# 5 2H 2D 4C 4D 4S
# Full House
# With Three Fours
# 3C 3D 3S 9S 9D
# Full House
# with Three Threes
# Winner Player 1

# The file, poker.txt, contains one-thousand random hands dealt to two
# players. Each line of the file contains ten cards (separated by a single
# space): the first five are Player 1's cards and the last five are Player 2's
# cards. You can assume that all hands are valid (no invalid characters or
# repeated cards), each player's hand is in no specific order, and in each hand
# there is a clear winner.

# How many hands does Player 1 win?

import sys
import string

class Card(object):
  kinds = {'2': 'Two', '3': 'Three', '4': 'Four', '5': 'Five', '6': 'Six',
           '7': 'Seven', '8': 'Eight', '9': 'Nine', 'T': 'Ten',
           'J': 'Jack', 'Q': 'Queen', 'K': 'King', 'A': 'Ace'}
  suits = {'H': 'Hearts', 'C': 'Clubs', 'S': 'Spades', 'D': 'Diamonds'}

  def __init__(self, val):
    assert len(val) == 2
    assert val[0] in Card.kinds.keys()
    assert val[1] in Card.suits.keys()
    self.val = val

  def _order(self):
    return '23456789TJQKA'.index(self.val[0])

  def __cmp__(self, other):
    return self._order() - other._order()

  @property
  def kind(self):
    return Card.kinds[self.val[0]]

  @property
  def suit(self):
    return Card.suits[self.val[1]]

  def __str__(self):
    return '%s %s (%s)' % (self.kind, self.suit, self.val)

  def __repr__(self):
    return self.__str__()
  

class Hand(object):
  def __init__(self, cards):
    assert len(cards) == 5
    self.cards = sorted(cards)[::-1]

  def __str__(self):
    return 'Hand {%s}' % ', '.join([str(card) for card in self.cards])


class Rank(object):
  def __init__(self, hand):
    self.val = self._ComputeValue(hand)

  def __str__(self):
    return 'Rank "%s" {%s}' % (
      ('High Card',
       'One Pair',
       'Two Pairs',
       'Three of a Kind',
       'Straight',
       'Flush',
       'Full House',
       'Four of a Kind',
       'Straight Flush',
       'Royal Flush')[self.val[0]],
      ', '.join([str(card) for card in self.val[1:]]))
      
  def __cmp__(self, other):
    assert self.val != other.val
    if (self.val > other.val):
      return 1
    assert self.val < other.val
    return -1

  def _ComputeValue(self, hand):
    suits = [card.suit for card in hand.cards]
    kinds = [card.kind for card in hand.cards]
    all_kinds = ['Ace', 'King', 'Queen', 'Jack', 'Ten', 'Nine',
                 'Eight', 'Seven', 'Six', 'Five', 'Four', 'Three', 'Two']
    is_same_suit = len(set(suits)) == 1

    highest_ind = all_kinds.index(hand.cards[0].kind)
    is_consecutive = False
    if highest_ind <= len(all_kinds) - len(hand.cards):
      for ind in xrange(len(hand.cards)):
        if hand.cards[ind].kind != all_kinds[highest_ind + ind]:
          break
      else:
        is_consecutive = True

    same_kind_lists = []
    same_kind_lists_map = {}
    for card in hand.cards:
      same_kind_lists_map.setdefault(card.kind, []).append(card)
    same_kind_lists = sorted(same_kind_lists_map.values(),
                             key=lambda l: (len(l), l[0]))[::-1]
    same_kind_cards = [cards[0] for cards in same_kind_lists]

    # Check for Royal Flush: Ace, King, Queen, Jack, Ten, in same suit.
    if (is_same_suit and is_consecutive and highest_ind == 0):
      return [9]

    # Straight Flush: All cards are consecutive values of same suit.
    if (is_same_suit and is_consecutive):
      return [8, hand.cards[0]]

    # Four of a Kind: Four cards of the same value.
    if len(same_kind_lists) == 2 and len(same_kind_lists[0]) == 4:
      return [7, same_kind_lists[0][0], same_kind_lists[1][0]]

    # Full House: Three of a kind and a pair.
    if len(same_kind_lists) == 2 and len(same_kind_lists[0]) == 3:
      return [6, same_kind_lists[0][0], same_kind_lists[1][0]]

    # Flush: All cards of the same suit.
    if is_same_suit:
      ret = [5]
      ret.extend(hand.cards)
      return ret

    # Straight: All cards are consecutive values.
    if is_consecutive:
      return [4, hand.cards[0]]

    # Three of a Kind: Three cards of the same value.
    if len(same_kind_lists) == 3 and len(same_kind_lists[0]) == 3:
      assert len(same_kind_lists[1]) == 1
      assert len(same_kind_lists[2]) == 1
      ret = [3]
      ret.extend(same_kind_cards)
      return ret

    # Two Pairs: Two different pairs.
    if len(same_kind_lists) == 3 and len(same_kind_lists[0]) == 2:
      assert len(same_kind_lists[1]) == 2
      assert len(same_kind_lists[2]) == 1
      ret = [2]
      ret.extend(same_kind_cards)
      return ret
    
    # One Pair: Two cards of the same value.
    if len(same_kind_lists) == 4:
      assert len(same_kind_lists[0]) == 2
      assert len(same_kind_lists[1]) == 1
      ret = [1]
      ret.extend(same_kind_cards)
      return ret

    # High Card: Highest value card.
    assert len(same_kind_lists) == 5
    ret = [0]
    ret.extend(hand.cards)
    return ret
  

def ReadHands(line):
  coded_cards = line.split()
  assert len(coded_cards) == 10
  tom = Hand([Card(c) for c in coded_cards[:5]])
  jerry = Hand([Card(c) for c in coded_cards[5:]])
  rank_tom = Rank(tom)
  rank_jerry = Rank(jerry)
  first_wins = rank_tom > rank_jerry  

  print tom
  print rank_tom
  print 'vs'
  print jerry
  print rank_jerry
  print 'first wins:', first_wins

  print
  print

  return int(first_wins)

def OpenFile():
  if len(sys.argv) < 2:
    print 'Usage:', sys.argv[0], '<file>'
    exit(1)
  try:
    f = open(sys.argv[1], 'r')
  except IOError,e:
    print 'Cannot open file:', sys.argv[1], e
    exit(1)
  return f

# ReadHands('5H 5C 6S 7S KD 2C 3S 8S 8D TD')
# ReadHands('5D 8C 9S JS AC 2C 5C 7D 8S QH')
# ReadHands('2D 9C AS AH AC 3D 6D 7D TD QD')
# ReadHands('4D 6S 9H QH QC 3D 6D 7H QD QS')
# ReadHands('2H 2D 4C 4D 4S 3C 3D 3S 9S 9D')
# ReadHands('2H 4D 3C 7D 5S 5C 4D 3S 3D 2D')

count = 0
for line in OpenFile():
  count += ReadHands(line)

print 'Result:', count

import random
from colors import *


class Card:
  def __init__(self, card_type: str):
    self.card_type = card_type


class ColoredCard(Card):
  def __init__(self, card_type: str, color: str):
    Card.__init__(self, card_type)
    self.color = color


class NumberCard(ColoredCard):
	def __init__(self, card_type: str, color: str, number: int):
		ColoredCard.__init__(self, card_type, color)
		self.number = number

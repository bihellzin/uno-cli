from cards import *
from colors import *
from speaker import *
from deck import *


class Game:
	def __init__(self):
		self.player_order = []
		self.deck = Deck()


class Rules:
	@staticmethod
	def reverse_card_played(self, game: Game):
		if game.deck.top_of_stack_card.card_type == 'reverse':
			self.player_order.reverse()

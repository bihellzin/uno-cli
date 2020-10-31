from cards import *
from colors import *
from speaker import *
from deck import *


class Game:
	def __init__(self):
		self.player_order = []
		self.deck = Deck()


	def playing(self):
		while not has_winner:
			for i in range(player_order):
				self.play(player_order[i])

				self.check_card_played()


	def play(self, player: Player):
		card = input("Play a card !\n")
		self.player.deck.pop(int(card))


	def check_card_played(self):
		pass


	# Rules
	@staticmethod
	def reverse_card_played(game: Game):
		if game.deck.top_of_stack_card.card_type == 'reverse':
			self.player_order.reverse()


	@staticmethod
	def skip_card_played(game: Game):
		if game.deck.top_of_stack_card.card_type == 'skip':
			self.player_order.reverse()


	@staticmethod
	def has_winner(game: Game):
		pass

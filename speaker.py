import pyttsx3

from colors import *
from cards import Card, ColoredCard, NumberCard


class Speaker:
	"""docstring for Speaker"""
	def __init__(self):
		self.engine = pyttsx3.init()


	def speak_wild_card(self, card: Card):
		self.engine.say(card.card_type)
		self.engine.runAndWait()
	

	def speak_colored_card(self, card: ColoredCard):
		color = self.check_color(card.color)
		self.engine.say(card.card_type)
		self.engine.say(color)
		self.engine.runAndWait()


	@staticmethod
	def check_color(color: str) -> str:
		if color == BLUE:
			return 'blue'

		elif color == RED:
			return 'red'

		elif color == GREEN:
			return 'green'

		elif color == YELLOW:
			return 'yellow'
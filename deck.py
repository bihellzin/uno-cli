from cards import *
from random import shuffle


class Deck:
    def __init__(self):
        self.deck = []
        self.stack = []

    def generate_deck(self):
        self.generate_colored_cards()
        self.generate_uncolored_cards()
        shuffle(self.deck)

    def generate_colored_cards(self):
        self.generate_number_cards()
        self.generate_special_colored_cards()

    def generate_number_cards(self):
        numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        colors = [BLUE, GREEN, RED, YELLOW]

        for number in numbers:
            for color in colors:
                if number == 0:
                    self.deck.append(NumberCard('number', color, number))

                else:
                    self.deck.append(NumberCard('number', color, number))
                    self.deck.append(NumberCard('number', color, number))

    def generate_special_colored_cards(self):
        card_types = ['draw plus 2', 'reverse', 'skip']
        colors = [BLUE, GREEN, RED, YELLOW]

        for card_type in card_types:
            for color in colors:
                self.deck.append(ColoredCard(card_type, color))
                self.deck.append(ColoredCard(card_type, color))

    def generate_uncolored_cards(self):
        card_types = ['wild', 'wild plus 4']

        for card_type in card_types:
            for i in range(4):
                self.deck.append(Card(card_type))

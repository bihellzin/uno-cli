from colors import *


class Card:
    def __init__(self, card_type: str):
        self.card_type = card_type

    def __str__(self) -> str:
        if self.card_type == 'wild':
            return RED + 'w' + YELLOW + 'i' + GREEN + 'l' + BLUE + 'd' + '\x1b[0m'

        else:
            return RED + 'w' + YELLOW + 'i' + GREEN + 'l' + BLUE + 'd draw 4' + '\x1b[0m'


class ColoredCard(Card):
    def __init__(self, card_type: str, color: str):
        Card.__init__(self, card_type)
        self.color = color


class NumberCard(ColoredCard):
    def __init__(self, card_type: str, color: str, number: int):
        ColoredCard.__init__(self, card_type, color)
        self.number = number

from colors import *
import pyttsx3


ENGINE = pyttsx3.init()

class Card:
    def __init__(self, card_type: str):
        self.card_type = card_type

    def __str__(self) -> str:
        if self.card_type == 'wild':
            return RED + 'w' + YELLOW + 'i' + GREEN + 'l' + BLUE + 'd' + '\x1b[0m'

        else:
            return RED + 'w' + YELLOW + 'i' + GREEN + 'l' + BLUE + 'd draw 4' + '\x1b[0m'

    
    def speak_card(self):
        ENGINE.say(self.card_type)
        ENGINE.runAndWait()


class ColoredCard(Card):
    def __init__(self, card_type: str, color: str):
        Card.__init__(self, card_type)
        self.color = color

    
    def speak_card(self):
        ENGINE.say(self.card_type)
        ENGINE.runAndWait()


class NumberCard(ColoredCard):
    def __init__(self, card_type: str, color: str, number: int):
        ColoredCard.__init__(self, card_type, color)
        self.number = number


    def speak_card(self):
        ENGINE.say(self.card_type)
        ENGINE.runAndWait()

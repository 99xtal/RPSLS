from player import Player
import random

class AI(Player):
    def __init__(self):
        super().__init__("Al the AI")

    def choose_gesture(self):
        choice = random.choice(self.gestures)
        self.gesture_choice = choice
        print(f'{self.name} picked {choice.name}')
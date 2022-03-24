from rock import Rock
from paper import Paper
from scissors import Scissors
from lizard import Lizard
from spock import Spock

class Player:
    def __init__(self, name):
        self.gestures = [Rock(), Paper(), Scissors(), Lizard(), Spock()]
        self.gesture_choice = Rock()
        self.name = name
        self.score = 0

    def choose_gesture(self):
        pass

    def print_gestures(self):
        print("\nOptions: ")
        for gesture in self.gestures:
            print(gesture.name)
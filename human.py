from player import Player

class Human(Player):
    def __init__(self):
        super().__init__()

    def set_name(self):
        self.name = input("Name: ")

    def choose_gesture(self):
        # input choice function
        while True:
            print("\nOPTIONS:")
            for each in self.gestures:
                print(each)
            choice = input(f"\n{self.name}, choose an option: ").lower()
            if choice in self.gestures:
                self.gesture_choice = choice
                break
            else:
                print("Oops! Please type one of the options!")
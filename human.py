from player import Player

class Human(Player):
    def __init__(self, name):
        super().__init__(name)

    def set_name(self):
        print(f"{self.name}, please enter your name.")
        self.name = input("Name: ")

    def choose_gesture(self):
        # input choice function
        counter = 0
        while counter != 1:
            self.print_gestures()

            choice = input(f"\n{self.name}, choose an option: ").lower()

            for gesture in self.gestures:
                if choice == gesture.name:
                    self.gesture_choice = gesture
                    counter = 1

            if self.gesture_choice.name != choice:
                print("Oops! Please type one of the options!")


from player import Player
from ai import AI

class Game:
    def __init__(self):
        self.player = Player()
        self.opponent = None
        self.combinations = {}
    
    def run_game(self):
        self.display_welcome()
        self.choose_game_mode()
        self.set_combinations()
        self.battle()
        self.display_winner()

    def display_welcome(self):
        print("Hello! Welcome to Rock, Paper, Scissors, Lizard, Spock")

    def battle(self):
        while self.player.score < 2 and self.opponent.score < 2:
            self.player.choose_gesture()
            self.opponent.choose_gesture()
            winner = self.choose_winner()
            if winner == None:
                print(f'\nNobody wins!')
            else:
                print(f'\n{winner.name} won the round')
                winner.score += 1
                print(f'{winner.name} has a score of {winner.score}')

    def choose_winner(self):
        opt1 = self.player.gesture_choice
        opt2 = self.opponent.gesture_choice
        win = f'{opt1}{opt2}'
        return self.combinations[win]
        
    def set_combinations(self):
        self.combinations = {"rockrock": None,
                            "rockpaper": self.opponent,
                            "rockscissors": self.player,
                            "rocklizard": self.player,
                            "rockspock": self.opponent,
                            "paperrock": self.player,
                            "paperpaper": None,
                            "paperscissors": self.opponent,
                            "paperlizard": self.opponent,
                            "paperspock": self.player,
                            "scissorsrock": self.opponent,
                            "scissorspaper": self.player,
                            "scissorsscissors": None,
                            "scissorslizard": self.player,
                            "scissorsspock": self.opponent,
                            "lizardrock": self.opponent,
                            "lizardpaper": self.player,
                            "lizardscissors": self.opponent,
                            "lizardlizard": None,
                            "lizardspock": self.player,
                            "spockrock": self.player,
                            "spockpaper": self.opponent,
                            "spockscissors": self.player,
                            "spocklizard": self.opponent,
                            "spockspock": None}
    
    def choose_game_mode(self):
        while True:
            game_choice = input("Would you like a single player(1) or multiplayer game(2)? Type 1 or 2: ")
            print("Player 1, please enter your name.")
            self.player.set_name()
            if game_choice == "1":
                self.opponent = AI()
                break
            elif game_choice == "2":
                self.opponent = Player()
                print("Player 2, please enter your name.")
                self.opponent.set_name()
                break
            else:
                print("Please choose (1) or (2)")

    def display_winner(self):
        if self.player.score == 2:
            print(f"{self.player.name} wins!\n")
        if self.opponent.score == 2:
            print(f"{self.opponent.name} wins!\n")
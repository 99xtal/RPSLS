from player import Player
from ai import AI

class Game:
    def __init__(self):
        self.player = Player("Player 1")
        self.opponent = None
        self.combinations = {}
    
    def run_game(self):
        self.display_welcome()
        self.choose_game_mode()
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
        
        
        # self.player.gesture_choice    self.opponent.gesture_choice

    def choose_winner(self):
        opt1 = self.player.gesture_choice
        opt2 = self.opponent.gesture_choice
        win = f'{opt1}{opt2}'
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
        return self.combinations[win]
        

    def choose_game_mode(self):
        while True:
            game_choice = input("Would you like a single player(1) or multiplayer game(2)? Type 1 or 2: ")
            if game_choice == "1":
                self.opponent = AI()
                break
            elif game_choice == "2":
                self.opponent = Player("Player 2")
                break
            else:
                print("Please choose (1) or (2)")

    def display_winner(self):
        if self.player.score == 2:
            print("Player 1 wins!\n")
        if self.opponent.score == 2:
            print("Player 2 wins!\n")

rpsls = Game()
rpsls.run_game()


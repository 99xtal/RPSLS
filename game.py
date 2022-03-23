from player import Player
from ai import AI

class Game:
    def __init__(self):
        self.player = Player()
        self.opponent = None
    
    def run_game(self):
        # display_welcome()
        # choose_game_mode()
        pass

    def display_welcome(self):
        print("Hello! Welcome to Rock, Paper, Scissors, Lizard, Spock")

    def battle(self):
        pass

    def player_turn(self):
        pass

    def opponent_turn(self):
        pass

    def choose_game_mode(self):
        game_choice = input("Would you like a single player(1) or multiplayer game(2)? Type 1 or 2")
        if game_choice == "1":
            self.opponent = AI()
        elif game_choice == "2":
            self.opponent = Player()

    def display_winner(self):
        pass
import random

RULES = {"rps": {"rock": ("scissors",),
                 "scissors": ("paper",),
                 "paper": ("rock",),
                 },
         "rpsls": {"rock": ("scissors", "lizard"),
                   "scissors": ("paper", "lizard"),
                   "paper": ("rock", "spock"),
                   "lizard": ("paper", "spock"),
                   "spock": ("rock", "scissors"),
                   },
         }


class PlayerObject:
    def __init__(self, name, rules=None):
        if rules is None:
            rules = RULES["rps"]
        self.rules = rules
        if name.lower() in self.rules.keys():
            self.name = name.lower()

        else:
            self.name = None

    def __repr__(self):
        return f"PlayerObject({self.name})"

    def __gt__(self, other):
        return other.name in self.rules[self.name]

    def __eq__(self, other):
        return self.name == other.name

    def random_object(self):
        return random.choice(list(self.rules.keys()))


class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.current_object = None

    def reset_object(self):
        self.current_object = None

    def win_round(self):
        self.score += 1

    def __repr__(self):
        return f"Player(Name: {self.name}, Score: {self.score}"


class HumanPlayer(Player):
    def choose_object(self, choice):
        self.current_object = PlayerObject(choice)


class ComputerPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.name = "Computer"
        self.current_object = PlayerObject("Computer")

    def choose_object(self):
        self.current_object.random_object()


class Game:
    def __init__(self):
        self.current_round = 0
        self.max_rounds = 10
        self.players = []
        self.round_result = None
        self.round_winner = None


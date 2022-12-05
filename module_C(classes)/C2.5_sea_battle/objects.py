EMPTY = 0
SHIP = 1
SHOTTED_MISS = 2
SHOTTED_HIT = 3


class Ship:

    def __init__(self, length, head_xy, orient):
        self.length = length
        self.head_xy = head_xy
        self.orientation = orient
        self.lives = length


class Cell:

    def __init__(self, x, y):
        self.state = EMPTY
        self.x = x
        self.y = y


class Board:

    def __init__(self):
        self.board_matrix = []
        self.three_deck_count = 0
        self.two_deck_count = 0
        self.one_deck_count = 0

    def draw(self):
        pass

    def place_ship(self):
        pass

    def make_contour(self):
        pass

    def shot(self):
        pass


class Player:

    def __init__(self, name):
        self.name = name
        self.mine_board = None
        self.enemy_board = None

    def ask_move(self):
        pass

    def shoot(self):
        pass


class User(Player):

    def ask_move(self):
        pass

    def shoot(self):
        pass


class AI(Player):
    def ask_move(self):
        pass

    def shoot(self):
        pass


class Game:
    def __init__(self, user, user_board, ai, ai_board):
        self.user = user
        self.user_board = user_board
        self.ai = ai
        self.ai_board = ai_board

    def place_ships(self):
        pass

    def hello(self):
        pass

    def game_loop(self):
        pass

    def start(self):
        pass

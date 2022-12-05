import random

EMPTY = 0
SHIP = 1
NEAR_SHIP = 2
SHOTTED_MISS = 3
SHOTTED_HIT = 4
HORIZONTAL = 0
VERTICAL = 1


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

    def __init__(self, hide):
        self.board_matrix = [[Cell(i, j) for i in range(6)] for j in range(6)]
        self.three_deck_count = 1
        self.two_deck_count = 2
        self.one_deck_count = 3
        self.hide = hide

    def draw(self):
        print('    1   2   3   4   5   6')
        for i in range(6):
            print(i + 1, end=' | ')
            for j in range(6):
                if self.board_matrix[i][j].state == EMPTY:
                    label = chr(8413)
                elif self.board_matrix[i][j].state == SHIP:
                    if self.hide:
                        label = chr(8413)
                    else:
                        label = chr(8419)
                elif self.board_matrix[i][j].state == SHOTTED_MISS:
                    label = chr(8416)
                elif self.board_matrix[i][j].state == SHOTTED_HIT:
                    label = chr(8999)
                print(label, ' | ', end='')
            print()

    def place_ship(self, ship):
        x = ship.head_xy[0]
        y = ship.head_xy[1]
        self.board_matrix[x][y].state = SHIP
        for i in range(1, ship.length):
            if ship.orientation == HORIZONTAL:
                self.board_matrix[x + i][y].state = SHIP
            else:
                self.board_matrix[x][y + i].state = SHIP


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
        self.user_ships = []
        self.ai_ships = []

    def draw_boards(self):
        print('        Мое поле                          Поле компьютера')
        print('    1   2   3   4   5   6             1   2   3   4   5   6')
        for i in range(6):
            print(i + 1, end=' | ')
            for j in range(6):
                if self.user_board.board_matrix[i][j].state == EMPTY:
                    label = chr(8413)
                elif self.user_board.board_matrix[i][j].state == SHIP:
                    if self.user_board.hide:
                        label = chr(8413)
                    else:
                        label = chr(8419)
                elif self.user_board.board_matrix[i][j].state == SHOTTED_MISS:
                    label = chr(8416)
                elif self.user_board.board_matrix[i][j].state == SHOTTED_HIT:
                    label = chr(8999)
                print(label, ' | ', end='')
            print('     ', i + 1, end=' | ')

            for j in range(6):
                if self.ai_board.board_matrix[i][j].state == EMPTY:
                    label = chr(8413)
                elif self.ai_board.board_matrix[i][j].state == SHIP:
                    if self.ai_board.hide:
                        label = chr(8413)
                    else:
                        label = chr(8419)
                elif self.ai_board.board_matrix[i][j].state == SHOTTED_MISS:
                    label = chr(8416)
                elif self.ai_board.board_matrix[i][j].state == SHOTTED_HIT:
                    label = chr(8999)
                print(label, ' | ', end='')
            print()

    def place_ships(self):
        while True:
            for i in range(self.user_board.three_deck_count):
                orient = random.randint(0, 1)
                if orient:
                    x = random.randint(0, 5)
                    y = random.randint(0, 3)
                    self.user_ships.append(Ship(3, (x, y), orient=VERTICAL))
                else:
                    x = random.randint(0, 3)
                    y = random.randint(0, 5)
                    self.user_ships.append(Ship(3, (x, y), orient=HORIZONTAL))
            for ship in self.user_ships:
                self.user_board.place_ship(ship)



    def hello(self):
        pass

    def game_loop(self):
        pass

    def start(self):
        pass


my_board = Board(hide=False)
ai_board = Board(hide=True)
player = User(name='Игрок')
ai = AI(name='Компьютер')
#my_board.draw()
game = Game(player, my_board, ai, ai_board)
game.place_ships()
game.draw_boards()

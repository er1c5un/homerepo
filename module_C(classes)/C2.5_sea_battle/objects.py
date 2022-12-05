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

    def __init__(self, hide):
        self.board_matrix = [[Cell(i, j) for i in range(6)] for j in range(6)]
        self.three_deck_count = 0
        self.two_deck_count = 0
        self.one_deck_count = 0
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

    def draw_boards(self):
        print('        Мое поле                          Поле компьютера')
        print('    1   2   3   4   5   6             1   2   3   4   5   6')
        for i in range(6):
            print(i + 1, end=' | ')
            for j in range(6):
                if self.user_board.board_matrix[i][j].state == EMPTY:
                    label = chr(8413)
                elif self.user_board.board_matrix[i][j].state == SHIP:
                    if self.hide:
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
                    if self.hide:
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
        pass

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
game.draw_boards()

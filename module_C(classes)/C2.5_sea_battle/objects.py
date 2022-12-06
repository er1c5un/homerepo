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

    def make_contour(self, new_ship):
        if new_ship.orientation == VERTICAL:
            for i in range(-1, new_ship.length + 1):
                for j in range(-1, 2):
                    try:
                        x = new_ship.head_xy[0] + i
                        y = new_ship.head_xy[1] + j
                        if x >= 0 and y >= 0:
                            if self.board_matrix[x][y].state == EMPTY:
                                self.board_matrix[x][y].state = NEAR_SHIP
                    except IndexError as ie:
                        pass
        else:
            for i in range(-1, 2):
                for j in range(-1, new_ship.length + 1):
                    try:
                        x = new_ship.head_xy[0] + i
                        y = new_ship.head_xy[1] + j
                        if x >= 0 and y >= 0:
                            if self.board_matrix[x][y].state == EMPTY:
                                self.board_matrix[x][y].state = NEAR_SHIP
                    except IndexError as ie:
                        pass

    def place_ship(self, ship):
        x = ship.head_xy[0]
        y = ship.head_xy[1]
        if self.board_matrix[x][y].state == EMPTY:
            if ship.orientation == HORIZONTAL:
                print("HORIZONTAL SHIP")
                for i in range(1, ship.length):
                    print(f"x {x}, y {y}, i {i}")
                    if self.board_matrix[x][y + i].state != EMPTY:
                        raise ValueError(f"Корабль не может быть размещен, клетка {x} {y + i} занята")
            else:
                print("VERTICAL SHIP")
                for i in range(1, ship.length):
                    print(f"x {x}, i {i}, y {y}")
                    if self.board_matrix[x + i][y].state != EMPTY:
                        raise ValueError(f"Корабль не может быть размещен, клетка {x + i} {y} занята")
            self.board_matrix[x][y].state = SHIP
            for i in range(1, ship.length):
                if ship.orientation == HORIZONTAL:
                    self.board_matrix[x][y + i].state = SHIP
                else:
                    self.board_matrix[x + i][y].state = SHIP
        else:
            raise ValueError(f"Корабль не может быть размещен, клетка носа {x} {y} корабля занята")
        self.make_contour(ship)

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


def place_ship(deck, count, board, ship_list):
    for i in range(count):
        count_tries = 0
        while True:
            try:
                orient = random.randint(0, 1)
                if orient:
                    x = random.randint(0, 5 - (deck - 1))
                    y = random.randint(0, 5)
                    ship = Ship(deck, (x, y), orient=VERTICAL)
                    board.place_ship(ship)
                    ship_list.append(ship)
                    break
                else:
                    x = random.randint(0, 5)
                    y = random.randint(0, 5 - (deck - 1))
                    ship = Ship(deck, (x, y), orient=HORIZONTAL)
                    board.place_ship(ship)
                    ship_list.append(ship)
                    break
            except ValueError as e:
                print(f"Корабль не может быть размещен, попытка {count_tries}")
                print(f"Error: {e}")
            if count_tries > 1000:
                raise ValueError("Не вышло инициализировать доску, доска неудачна")
                break
            else:
                count_tries += 1
    #return ship_list

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
                elif self.user_board.board_matrix[i][j].state == NEAR_SHIP:
                    if self.user_board.hide:
                        label = chr(8413)
                    else:
                        label = chr(8413)#chr(8416)
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
                elif self.ai_board.board_matrix[i][j].state == NEAR_SHIP:
                    if self.ai_board.hide:
                        label = chr(8413)
                    else:
                        label = chr(8413)#chr(8416)
                elif self.ai_board.board_matrix[i][j].state == SHOTTED_MISS:
                    label = chr(8416)
                elif self.ai_board.board_matrix[i][j].state == SHOTTED_HIT:
                    label = chr(8999)
                print(label, ' | ', end='')
            print()

    def place_ships(self, brd: Board, usr: Player):
        if isinstance(usr, User):
            place_ship(deck=3, count=brd.three_deck_count, board=brd, ship_list=self.user_ships)
            place_ship(deck=2, count=brd.two_deck_count, board=brd, ship_list=self.user_ships)
            place_ship(deck=1, count=brd.one_deck_count, board=brd, ship_list=self.user_ships)
        else:
            place_ship(deck=3, count=brd.three_deck_count, board=brd, ship_list=self.ai_ships)
            place_ship(deck=2, count=brd.two_deck_count, board=brd, ship_list=self.ai_ships)
            place_ship(deck=1, count=brd.one_deck_count, board=brd, ship_list=self.ai_ships)

    def hello(self):
        pass

    def game_loop(self):
        pass

    def start(self):
        pass


count_of_tries = 0
while True:
    try:
        my_board = Board(hide=False)
        ai_board = Board(hide=False)
        player = User(name='Игрок')
        ai = AI(name='Компьютер')
        # my_board.draw()
        game = Game(player, my_board, ai, ai_board)
        game.place_ships(my_board, player)
        game.place_ships(ai_board, ai)
        break
    except ValueError as ve:
        print('Не удалось расставить корабли, пробуем еще.')
    if count_of_tries > 10:
        raise ValueError('Не удалось проинициализровать доску, 1000 попыток')
        break
    else:
        count_of_tries += 1
game.draw_boards()
print("END")

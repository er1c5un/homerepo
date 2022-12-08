import os
import random
import enum


class State(enum.Enum):
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
        self.is_alive = True

    def ship_hitted(self):
        self.lives -= 1
        if self.lives == 0:
            self.is_alive = False


class Cell:

    def __init__(self, x, y):
        self.state = State.EMPTY
        self.x = x
        self.y = y
        self.ship_link = None  # ссылка на корабль, размещенный в данной клетке. Для удобства поиска корабля при стрельбе по клетке.


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
                if self.board_matrix[i][j].state == State.EMPTY:
                    label = chr(8413)
                elif self.board_matrix[i][j].state == State.SHIP:
                    if self.hide:
                        label = chr(8413)
                    else:
                        label = chr(8419)
                elif self.board_matrix[i][j].state == State.SHOTTED_MISS:
                    label = chr(8416)
                elif self.board_matrix[i][j].state == State.SHOTTED_HIT:
                    label = chr(8999)
                print(label, ' | ', end='')
            print()

    def make_contour(self, new_ship):
        if new_ship.orientation == State.VERTICAL:
            for i in range(-1, new_ship.length + 1):
                for j in range(-1, 2):
                    try:
                        x = new_ship.head_xy[0] + i
                        y = new_ship.head_xy[1] + j
                        if x >= 0 and y >= 0:
                            if self.board_matrix[x][y].state == State.EMPTY:
                                self.board_matrix[x][y].state = State.NEAR_SHIP
                    except IndexError as ie:
                        pass
        else:
            for i in range(-1, 2):
                for j in range(-1, new_ship.length + 1):
                    try:
                        x = new_ship.head_xy[0] + i
                        y = new_ship.head_xy[1] + j
                        if x >= 0 and y >= 0:
                            if self.board_matrix[x][y].state == State.EMPTY:
                                self.board_matrix[x][y].state = State.NEAR_SHIP
                    except IndexError as ie:
                        pass

    def place_ship(self, ship):
        x = ship.head_xy[0]
        y = ship.head_xy[1]
        if self.board_matrix[x][y].state == State.EMPTY:
            if ship.orientation == State.HORIZONTAL:
                # print("HORIZONTAL SHIP")
                for i in range(1, ship.length):
                    # print(f"x {x}, y {y}, i {i}")
                    if self.board_matrix[x][y + i].state != State.EMPTY:
                        raise ValueError(f"Корабль не может быть размещен, клетка {x} {y + i} занята")
            else:
                # print("VERTICAL SHIP")
                for i in range(1, ship.length):
                    # print(f"x {x}, i {i}, y {y}")
                    if self.board_matrix[x + i][y].state != State.EMPTY:
                        raise ValueError(f"Корабль не может быть размещен, клетка {x + i} {y} занята")
            self.board_matrix[x][y].state = State.SHIP
            self.board_matrix[x][
                y].ship_link = ship  # размещаем у клетки ссылку на корабль, для более удобного поиска при выстрелах
            for i in range(1, ship.length):
                if ship.orientation == State.HORIZONTAL:
                    self.board_matrix[x][y + i].state = State.SHIP
                    self.board_matrix[x][y + i].ship_link = ship
                else:
                    self.board_matrix[x + i][y].state = State.SHIP
                    self.board_matrix[x + i][y].ship_link = ship
        else:
            raise ValueError(f"Корабль не может быть размещен, клетка носа {x} {y} корабля занята")
        self.make_contour(ship)

    def shoot(self, x, y):
        x = x - 1  # уменьшаем на 1, так как в списке значения с 0
        y = y - 1
        print("SHOOT METHOD ON BOARD CLASS")
        if 0 <= x <= 5 and 0 <= y <= 5:
            cell = self.board_matrix[x][y]
            if cell.state == State.EMPTY or cell.state == State.NEAR_SHIP:
                # если выстрелили в пустую клетку без кораблей
                cell.state = State.SHOTTED_MISS
                return False  # возвращаем False, чтобы передать ход другому игроку
            elif cell.state == State.SHOTTED_MISS or cell.state == State.SHOTTED_HIT:
                # если выстрелили в клетку, по которой уже ранее стреляли
                raise ValueError("Вы сюда уже стреляли, введите другие координаты")
            elif cell.state == State.SHIP:
                cell.state = State.SHOTTED_HIT
                # cell.ship_link.lives -= 1
                cell.ship_link.ship_hitted()
                return True  # возвращаем True, чтобы игрок ходил повторно
        else:
            raise ValueError("Невалидные координаты клетки. Должны быть в пределах [1, 6]")


class Player:

    def __init__(self, name, mine_board, enemy_board):
        self.name = name
        self.mine_board = mine_board
        self.enemy_board = enemy_board

    def ask_move(self):
        pass

    def player_shoot(self):
        pass


class User(Player):

    def ask_move(self):
        aim = input("Ваш ход, куда стреляем? :")
        x = int(aim[0])
        y = int(aim[1])
        return x, y

    def player_shoot(self):
        while True:
            try:
                x, y = self.ask_move()
                self.enemy_board.shoot(x, y)
                break
            except ValueError as e:
                print(f"Невалидные координаты клетки: x = {x}, y = {y}")


class AI(Player):
    def ask_move(self):
        # рандом от 1 до 6, так как потом вычитаем единицу
        # сделано для того, чтобы пользователь выбирал клетки с 1 по 6
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return x, y

    def player_shoot(self):
        while True:
            try:
                x, y = self.ask_move()
                self.enemy_board.shoot(x, y)
                break
            except ValueError as e:
                print(f"Невалидные координаты клетки: x = {x}, y = {y}")


def place_ship(deck, count, board, ship_list):
    for i in range(count):
        count_tries = 0
        while True:
            try:
                orient = random.randint(0, 1)
                if orient:
                    x = random.randint(0, 5 - (deck - 1))
                    y = random.randint(0, 5)
                    ship = Ship(deck, (x, y), orient=State.VERTICAL)
                    board.place_ship(ship)
                    ship_list.append(ship)
                    break
                else:
                    x = random.randint(0, 5)
                    y = random.randint(0, 5 - (deck - 1))
                    ship = Ship(deck, (x, y), orient=State.HORIZONTAL)
                    board.place_ship(ship)
                    ship_list.append(ship)
                    break
            except ValueError as e:
                # print(f"Корабль не может быть размещен, попытка {count_tries}")
                # print(f"Error: {e}")
                pass
            if count_tries > 1000:
                raise ValueError("Не вышло инициализировать доску, доска неудачна")
                break
            else:
                count_tries += 1
    # return ship_list


def print_cell(label: str, spaces: int):
    if spaces == 3:
        print(f'|{label: ^3}', sep='', end='')
    elif spaces == 4:
        print(f'|{label: ^4}', sep='', end='')


class Game:
    def __init__(self, user, user_board, ai, ai_board):
        self.user = user
        self.user_board = user_board
        self.ai = ai
        self.ai_board = ai_board
        self.user_ships = []
        self.ai_ships = []

    def count_alive_ships(self, ship_list, deck):
        count = 0
        for ship in ship_list:
            if ship.is_alive and ship.length == deck:
                count += 1
        return count

    def draw_boards(self):
        # s.system('cls||clear')
        print('Мое поле                         Поле компьютера')
        print("Осталось кораблей:               Осталось кораблей:")
        print("3-х палубных -", self.count_alive_ships(self.user_ships, 3), "                3-х палубных -",
              self.count_alive_ships(self.ai_ships, 3))
        print("2-х палубных -", self.count_alive_ships(self.user_ships, 2), "                2-х палубных -",
              self.count_alive_ships(self.ai_ships, 2))
        print("1-х палубных -", self.count_alive_ships(self.user_ships, 1), "                1-х палубных -",
              self.count_alive_ships(self.ai_ships, 1))

        print()
        print('    1   2   3   4   5   6            1   2   3   4   5   6')
        for i in range(6):
            print(i + 1, end=' ')
            for j in range(6):
                if self.user_board.board_matrix[i][j].state == State.EMPTY:
                    label = chr(8413)
                    print_cell(label=label, spaces=4)
                elif self.user_board.board_matrix[i][j].state == State.SHIP:
                    if self.user_board.hide:
                        label = chr(8413)
                        print_cell(label=label, spaces=3)
                    else:
                        label = chr(9632)
                        print_cell(label=label, spaces=3)
                elif self.user_board.board_matrix[i][j].state == State.NEAR_SHIP:
                    if self.user_board.hide:
                        label = chr(8413)
                        print_cell(label=label, spaces=4)
                    else:
                        label = chr(8413)
                        print_cell(label=label, spaces=4)
                elif self.user_board.board_matrix[i][j].state == State.SHOTTED_MISS:
                    label = chr(8416)
                    print_cell(label=label, spaces=4)
                elif self.user_board.board_matrix[i][j].state == State.SHOTTED_HIT:
                    label = chr(9746)  # chr(8999)
                    print_cell(label=label, spaces=3)

            print('|     ', i + 1, end=' ')

            for j in range(6):
                if self.ai_board.board_matrix[i][j].state == State.EMPTY:
                    label = chr(8413)
                    print_cell(label=label, spaces=4)
                elif self.ai_board.board_matrix[i][j].state == State.SHIP:
                    if self.ai_board.hide:
                        label = chr(8413)
                        print_cell(label=label, spaces=4)
                    else:
                        label = chr(9632)
                        print_cell(label=label, spaces=3)
                elif self.ai_board.board_matrix[i][j].state == State.NEAR_SHIP:
                    if self.ai_board.hide:
                        label = chr(8413)
                        print_cell(label=label, spaces=4)
                    else:
                        label = chr(8413)
                        print_cell(label=label, spaces=4)  # chr(8416)
                elif self.ai_board.board_matrix[i][j].state == State.SHOTTED_MISS:
                    label = chr(8416)
                    print_cell(label=label, spaces=4)
                elif self.ai_board.board_matrix[i][j].state == State.SHOTTED_HIT:
                    label = chr(9746)  # chr(8999)
                    print_cell(label=label, spaces=3)

            print('|')

    def place_ships(self, brd: Board, usr: Player):
        if isinstance(usr, User):
            place_ship(deck=3, count=brd.three_deck_count, board=brd, ship_list=self.user_ships)
            place_ship(deck=2, count=brd.two_deck_count, board=brd, ship_list=self.user_ships)
            place_ship(deck=1, count=brd.one_deck_count, board=brd, ship_list=self.user_ships)
        else:
            place_ship(deck=3, count=brd.three_deck_count, board=brd, ship_list=self.ai_ships)
            place_ship(deck=2, count=brd.two_deck_count, board=brd, ship_list=self.ai_ships)
            place_ship(deck=1, count=brd.one_deck_count, board=brd, ship_list=self.ai_ships)

    def is_player_win(self, player_to_check):
        all_ships_dead = True
        if player_to_check == "User":
            enemy_ships = self.ai_ships
        else:
            enemy_ships = self.user_ships
        for ship in enemy_ships:
            if ship.is_alive:
                all_ships_dead = False
        return all_ships_dead

    def is_end_game(self):
        # проверяем на победу юзера (подбиты ли все корабли бота)
        if self.is_player_win(player_to_check="User"):
            print("Вы победили!")
            return True
        # проверяем на победу бота (подбиты ли все корабли юзера)
        elif self.is_player_win(player_to_check="AI"):
            print("Вы проиграли...")
            return True
        else:
            return False

    def hello(self):
        pass

    def game_loop(self):
        user_turn = True
        while True:
            if user_turn:
                self.draw_boards()
                user_turn = self.user.player_shoot()
                if self.is_end_game():
                    break
            else:
                user_turn = not self.ai.player_shoot()
                if self.is_end_game():
                    break

    def start(self):
        self.hello()
        self.game_loop()


count_of_tries = 0
while True:
    try:
        my_board = Board(hide=False)
        ai_board = Board(hide=True)
        player = User(name='Игрок', mine_board=my_board, enemy_board=ai_board)
        ai = AI(name='Компьютер', mine_board=ai_board, enemy_board=my_board)
        # my_board.draw()
        game = Game(player, my_board, ai, ai_board)
        game.place_ships(my_board, player)
        game.place_ships(ai_board, ai)
        break
    except ValueError as ve:
        pass
        # print('Не удалось расставить корабли, пробуем еще.')
    if count_of_tries > 10:
        raise ValueError('Не удалось проинициализровать доску, 1000 попыток')
        break
    else:
        count_of_tries += 1
# game.draw_boards()
game.start()
print("END")

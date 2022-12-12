import os
import random
import enum


class State(enum.Enum):
    """
    Класс для глоабльных параметров состояний клетки и ориентации кораблей
    """
    EMPTY = 0
    SHIP = 1
    NEAR_SHIP = 2
    SHOTTED_MISS = 3
    SHOTTED_HIT = 4
    HORIZONTAL = 0
    VERTICAL = 1


class Ship:

    def __init__(self, length: int, head_xy: tuple, orient: int):
        """
        :param length: длина коробля
        :param head_xy: координаты носа корабля, tuple (x,y)
        :param orient: ориентация корабля (1-вертикально\0-горизонтально)
        """
        self.length = length
        self.head_xy = head_xy
        self.orientation = orient
        self.lives = length  # количество оставшихся жизней корабля
        self.is_alive = True  # флаг, живой ли еще корабль

    def ship_hitted(self):
        """
        Метод, обрабатывающий попадание в корабль.
        Снимает одну жизнь.
        Если жизней не осталось, помечает корабль потопленным.
        """
        self.lives -= 1
        if self.lives == 0:
            self.is_alive = False


class Cell:

    def __init__(self, x: int, y: int):
        """
        :param x: координата ячейки (номер строки)
        :param y: координата ячейки (номер столбца)
        """
        self.state = State.EMPTY  # свойство, хранящее состояние ячейки
        self.x = x
        self.y = y
        self.ship_link = None  # ссылка на корабль, размещенный в данной клетке. Для удобства поиска корабля при стрельбе по клетке.


class Board:

    def __init__(self, hide: bool):
        self.board_matrix = [[Cell(i, j) for i in range(6)] for j in
                             range(6)]  # матрица игрового поля доски, содержит объекты класса Cell
        self.three_deck_count = 1  # количество 3-х палубных кораблей
        self.two_deck_count = 2  # количество 2-х палубных кораблей
        self.one_deck_count = 3  # количество 1 палубдных кораблей
        self.hide = hide  # свойство доски, нужно ли скрывать на экране расположение кораблей. True - скрываем

    def make_contour(self, new_ship: Ship):
        """
        Помечает контур корабля на поле, чтобы нельзя было размещать корабли в соседней клетке
        :param new_ship: Корабль, вокруг которого необходимо пометить клетки
        """
        if new_ship.orientation == State.VERTICAL:
            for i in range(-1, new_ship.length + 1):
                for j in range(-1, 2):
                    try:
                        x = new_ship.head_xy[0] + i
                        y = new_ship.head_xy[1] + j
                        if x >= 0 and y >= 0:
                            cell = self.board_matrix[x][y]
                            if cell.state == State.EMPTY:
                                cell.state = State.NEAR_SHIP
                    except IndexError as ie:
                        pass
        else:
            for i in range(-1, 2):
                for j in range(-1, new_ship.length + 1):
                    try:
                        x = new_ship.head_xy[0] + i
                        y = new_ship.head_xy[1] + j
                        if x >= 0 and y >= 0:
                            cell = self.board_matrix[x][y]
                            if cell.state == State.EMPTY:
                                cell.state = State.NEAR_SHIP
                    except IndexError as ie:
                        pass

    def place_ship(self, ship: Ship):
        """
        Размещает на доске корабль ship
        :param ship: объект класса Ship
        """
        x = ship.head_xy[0]
        y = ship.head_xy[1]
        cells = self.board_matrix
        if cells[x][y].state == State.EMPTY:
            if ship.orientation == State.HORIZONTAL:
                for i in range(1, ship.length):
                    if cells[x][y + i].state != State.EMPTY:
                        raise ValueError(f"Корабль не может быть размещен, клетка {x} {y + i} занята")
            else:
                for i in range(1, ship.length):
                    if cells[x + i][y].state != State.EMPTY:
                        raise ValueError(f"Корабль не может быть размещен, клетка {x + i} {y} занята")
            cells[x][y].state = State.SHIP
            cells[x][y].ship_link = ship  # размещаем у клетки ссылку на корабль, для более удобного поиска при выстрелах
            for i in range(1, ship.length):
                if ship.orientation == State.HORIZONTAL:
                    cells[x][y + i].state = State.SHIP
                    cells[x][y + i].ship_link = ship
                else:
                    cells[x + i][y].state = State.SHIP
                    cells[x + i][y].ship_link = ship
        else:
            raise ValueError(f"Корабль не может быть размещен, клетка носа {x} {y} корабля занята")
        self.make_contour(ship)

    def shoot(self, x: int, y: int):
        """
        Метод для выстрела по доске
        :param x: координата клетки (номер строки)
        :param y: координата клетки (номер столбца)
        return: True - игрок потворяет ход, False - ход переходит к следующему игроку
        """
        x = x - 1  # уменьшаем на 1, так как в списке значения с 0
        y = y - 1
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
                cell.ship_link.ship_hitted()
                return True  # возвращаем True, чтобы игрок ходил повторно
        else:
            raise ValueError("Невалидные координаты клетки. Должны быть в пределах [1, 6]")


class Player:

    def __init__(self, mine_board, enemy_board):
        """
        :param mine_board: своя доска игрока
        :param enemy_board: вражеская доска
        """
        self.mine_board = mine_board
        self.enemy_board = enemy_board

    def ask_move(self):
        pass

    def player_shoot(self):
        pass


class User(Player):

    def ask_move(self) -> tuple:
        """
        Запрашивает координаты выстрела
        :return: координаты выстрела, tuple (x,y)
        """
        aim = input("Ваш ход, куда стреляем? :")
        x = int(aim[0])
        y = int(aim[1])
        return x, y

    def player_shoot(self) -> bool:
        """
        Ход игрока, делает выстрел по вражеской доске
        :return: True - игрок ходит еще раз, False - переход хода
        """
        while True:
            try:
                x, y = self.ask_move()
                return self.enemy_board.shoot(x, y)
            except ValueError as e:
                print(f"Невалидные координаты клетки: x = {x}, y = {y}")


class AI(Player):
    def ask_move(self) -> tuple:
        """
        Запрос хода у компьютера. Ходит рандомно
        :return: координаты выстрела, tuple (x,y)
        """
        # рандом от 1 до 6, так как потом вычитаем единицу
        # сделано для того, чтобы пользователь выбирал клетки с 1 по 6
        x = random.randint(1, 6)
        y = random.randint(1, 6)
        return x, y

    def player_shoot(self):
        """
        Выстрел компьютера. Вызывает метод стрельбы по вражеской доске.
        :return: True - бот ходит еще раз, False - переход хода
        """
        while True:
            try:
                x, y = self.ask_move()
                return self.enemy_board.shoot(x, y)
            except ValueError as e:
                print(f"Невалидные координаты клетки: x = {x}, y = {y}")


def place_ship(deck: int, count: int, board: Board, ship_list: list):
    """
    Функция, которая создает нужно количество кораблей и размещает их на доске.
    :param deck: количество палуб корабля
    :param count: количество кораблей, которые необходимо расположить
    :param board: доска, на которой хотим расположить. Объект класса Board.
    :param ship_list: список кораблей, в который необходимо добавить расположенный успешно корабль
    """
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
            else:
                count_tries += 1
    # return ship_list


def print_cell(label: str, spaces: int):
    """
    Функция для форматированного вывода лейблов ячейки.
    :param label: Символ вывода состояния ячейки
    :param spaces: количество пробелов для равнения символа (некоторые символы юникода занимают больше места на экране)
    """
    if spaces == 3:
        print(f'|{label: ^3}', sep='', end='')
    elif spaces == 4:
        print(f'|{label: ^4}', sep='', end='')


class Game:
    def __init__(self, user: User, user_board: Board, ai: AI, ai_board: Board):
        """
        :param user: игрок
        :param user_board: доска игрока
        :param ai: бот
        :param ai_board: доска бота
        """
        self.user = user
        self.user_board = user_board
        self.ai = ai
        self.ai_board = ai_board
        self.user_ships = []
        self.ai_ships = []

    def count_alive_ships(self, ship_list: list, deck: int) -> int:
        """
        Метод для подсчета количества кораблей определенной палубности, которые остались в живых
        :param ship_list: список кораблей
        :param deck: количество палуб корабля
        :return:
        """
        count = 0
        for ship in ship_list:
            if ship.is_alive and ship.length == deck:
                count += 1
        return count

    def draw_boards(self):
        """
        Метод для отрисовки игровых полей
        """
        # s.system('cls||clear') # закомментировал, так как при запуске из pyCharm очистка консоли не работает
        print('Ваше поле                         Поле компьютера')
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
                user_cells = self.user_board.board_matrix
                if user_cells[i][j].state == State.EMPTY:
                    label = chr(8413)
                    print_cell(label=label, spaces=4)
                elif user_cells[i][j].state == State.SHIP:
                    if self.user_board.hide:
                        label = chr(8413)
                        print_cell(label=label, spaces=3)
                    else:
                        label = chr(9632)
                        print_cell(label=label, spaces=3)
                elif user_cells[i][j].state == State.NEAR_SHIP:
                    if self.user_board.hide:
                        label = chr(8413)
                        print_cell(label=label, spaces=4)
                    else:
                        label = chr(8413)
                        print_cell(label=label, spaces=4)
                elif user_cells[i][j].state == State.SHOTTED_MISS:
                    label = chr(8416)
                    print_cell(label=label, spaces=4)
                elif user_cells[i][j].state == State.SHOTTED_HIT:
                    label = chr(9746)
                    print_cell(label=label, spaces=3)

            print('|     ', i + 1, end=' ')

            for j in range(6):
                ai_cells = self.ai_board.board_matrix
                if ai_cells[i][j].state == State.EMPTY:
                    label = chr(8413)
                    print_cell(label=label, spaces=4)
                elif ai_cells[i][j].state == State.SHIP:
                    if self.ai_board.hide:
                        label = chr(8413)
                        print_cell(label=label, spaces=4)
                    else:
                        label = chr(9632)
                        print_cell(label=label, spaces=3)
                elif ai_cells[i][j].state == State.NEAR_SHIP:
                    if self.ai_board.hide:
                        label = chr(8413)
                        print_cell(label=label, spaces=4)
                    else:
                        label = chr(8413)
                        print_cell(label=label, spaces=4)
                elif ai_cells[i][j].state == State.SHOTTED_MISS:
                    label = chr(8416)
                    print_cell(label=label, spaces=4)
                elif ai_cells[i][j].state == State.SHOTTED_HIT:
                    label = chr(9746)
                    print_cell(label=label, spaces=3)
            print('|')

    def place_ships(self, brd: Board, usr: Player):
        """
        Метод для размещения кораблей. Используется для размещения кораблей игрока и компьютера
        :param brd: Доска, на которой нужно разместить корабли
        :param usr: Игрок, чьи корабли необходимо расположить
        """
        if isinstance(usr, User):
            place_ship(deck=3, count=brd.three_deck_count, board=brd, ship_list=self.user_ships)
            place_ship(deck=2, count=brd.two_deck_count, board=brd, ship_list=self.user_ships)
            place_ship(deck=1, count=brd.one_deck_count, board=brd, ship_list=self.user_ships)
        else:
            place_ship(deck=3, count=brd.three_deck_count, board=brd, ship_list=self.ai_ships)
            place_ship(deck=2, count=brd.two_deck_count, board=brd, ship_list=self.ai_ships)
            place_ship(deck=1, count=brd.one_deck_count, board=brd, ship_list=self.ai_ships)

    def is_player_win(self, player_to_check: str) -> bool:
        """
        Метод для проверки победы.
        :param player_to_check: Кого проверяем на победу. User - игрока, иначе - бота
        :return: True - победа, False - еще не победа
        """
        all_ships_dead = True
        if player_to_check == "User":
            enemy_ships = self.ai_ships
        else:
            enemy_ships = self.user_ships
        for ship in enemy_ships:
            if ship.is_alive:
                all_ships_dead = False
        return all_ships_dead

    def is_end_game(self) -> bool:
        """
        Метод для проверки, закончилась ли игра чьей-нибудь победой
        :return: True - игра окончена, False - игра не окончена
        """
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
        """
        Выводит правила игры
        """
        print("="*10, "ИГРА МОРСКОЙ БОЙ", "="*10)
        print()
        print("="*10, "Правила", "="*10)
        print("Вы играете против компьютера")
        print("Количество кораблей:")
        print("3-х палубных - 1")
        print("2-х палубных - 2")
        print("1-х палубных - 3")
        print("Корабли размещаются случайным образом")
        print("Корабль не может быть размещен на соседней клетке с другим кораблем")
        print("Чтобы сделать выстрел, введите 2 числа без пробелов")
        print("например так: 34, где 3 - номер строки, 4 - номер столбца клетки, куда хотим выстрелить")
        print("=" * 35)
        print("Удачи!")


    def game_loop(self):
        """
        Метод основного игрового цикла.
        По очереди делаем ходя игроков и проверяем на конец игры.
        """
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
        """
        Метод для запуска игры
        """
        self.hello()
        self.game_loop()

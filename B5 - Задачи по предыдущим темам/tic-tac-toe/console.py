def print_field(f: object):
    """
    Функция выводит на экран игровое поле
    :param f: матрица игрового поля
    """
    print('   ', 0, 1, 2, ' (х)')
    for i in range(3):
        print('', i, end='  ')
        for j in range(3):
            if f[i][j] == 1:
                sign = 'X'
            elif f[i][j] == 0:
                sign = 'O'
            else:
                sign = '-'
            print(sign, end=' ')
        print()
    print('(y)')


def check_lines(field: list) -> bool:
    """
    Проверяет, есть ли зачеркнутые строки в игровом поле
    :param field: матрица игрового поля
    :return: bool - зачеркивается линия или нет
    """
    for line in field:
        if line[0] and line[0] == line[1] == line[2]:
            return True
    return False


def check_columns(field: list) -> bool:
    """
    Проверяет, есть ли зачеркнутые столбца в игровом поле
    :param field: матрица игрового поля
    :return: bool
    """
    line1 = field[0]
    line2 = field[1]
    line3 = field[2]
    for i in range(3):
        if line1[i] and line1[i] == line2[i] == line3[i]:
            return True
    return False


def check_diagonal(field: list) -> bool:
    """
    Проверяет, есть ли зачеркнутые диагонали в игровом поле
    :param field: матрица игрового поля
    :return:
    """
    line1 = field[0]
    line2 = field[1]
    line3 = field[2]
    if line2[1] and (line1[0] == line2[1] == line3[2] or line1[2] == line2[1] == line3[0]):
        return True
    else:
        return False


def is_win(field: list) -> bool:
    """
    Проверяет, выиграл ли игрок
    :param field: матрица игрового поля
    :return:
    """
    lines_result = check_lines(field)
    if lines_result:
        return True
    columns_result = check_columns(field)
    if columns_result:
        return True
    diagonal_result = check_diagonal(field)
    if diagonal_result:
        return True
    return False


def next_player(player_num: int) -> int:
    """
    Производит смену игрока
    :param player_num: номер игрока
    :return:
    """
    return 0 if player_num else 1


player = 1
field = [['', '', ''] for _ in range(3)]

print('Координаты клетки вводятся в формате xy, где х - номер строки, y - номер столбца')


while True:
    while True:
        print_field(field)
        sign = 'X' if player else 'O'
        step = input(f'Ход игрока {player} ({sign}), введите координаты клетки :')
        x = int(step[0])
        y = int(step[1])
        if 0 <= x <= 2 and 0 <= y <= 2:
            if field[x][y] == '':
                break
            else:
                print('Клетка занята!')
        else:
            print('Введено значение за пределами поля!')
    field[x][y] = player

    if is_win(field):
        print(f'ПОБЕДИЛ ИГРОК {player}! Поздравляем!')
        print_field(field)
        if input('Хотите сыграть еще раз? (да/нет):').lower() in ['да', 'д', 'y', 'yes']:
            player = 1
            field = [['', '', ''] for _ in range(3)]
            print('Играем заново')
            print('-' * 30)
        else:
            print('Конец игры')
            break
    else:
        player = next_player(player)

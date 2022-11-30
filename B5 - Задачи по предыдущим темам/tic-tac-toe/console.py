def print_field(fld: object):
    """
    Функция выводит на экран игровое поле
    :param fld: матрица игрового поля
    """
    print('   ', 0, 1, 2, ' (y)')
    for i in range(3):
        print('', i, end='  ')
        for j in range(3):
            if fld[i][j] == 1:
                label = 'X'
            elif fld[i][j] == 0:
                label = 'O'
            else:
                label = '-'
            print(label, end=' ')
        print()
    print('(x)')


def check_lines(fld: list) -> bool:
    """
    Проверяет, есть ли зачеркнутые строки в игровом поле
    :param fld: матрица игрового поля
    :return: bool - зачеркивается линия или нет
    """
    for line in fld:
        if line[0] and line[0] == line[1] == line[2]:
            return True
    return False


def check_columns(fld: list) -> bool:
    """
    Проверяет, есть ли зачеркнутые столбца в игровом поле
    :param fld: матрица игрового поля
    :return: bool
    """
    line1 = fld[0]
    line2 = fld[1]
    line3 = fld[2]
    for i in range(3):
        if line1[i] and line1[i] == line2[i] == line3[i]:
            return True
    return False


def check_diagonal(fld: list) -> bool:
    """
    Проверяет, есть ли зачеркнутые диагонали в игровом поле
    :param fld: матрица игрового поля
    :return:
    """
    line1 = fld[0]
    line2 = fld[1]
    line3 = fld[2]
    if line2[1] and (line1[0] == line2[1] == line3[2] or line1[2] == line2[1] == line3[0]):
        return True
    else:
        return False


def is_win(fld: list) -> bool:
    """
    Проверяет, выиграл ли игрок
    :param fld: матрица игрового поля
    :return:
    """
    lines_result = check_lines(fld)
    if lines_result:
        return True
    columns_result = check_columns(fld)
    if columns_result:
        return True
    diagonal_result = check_diagonal(fld)
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

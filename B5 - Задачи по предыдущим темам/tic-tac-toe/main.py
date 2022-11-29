import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WIDTH = 300  # ширина игрового окна
HEIGHT = 500  # высота игрового окна


def draw_zero(scr: object, item: tuple) -> None:
    """
    Рисует нолики
    :param scr: экран pygame (Surface)
    :param item: кортеж с номером клетки игрового поля
    """
    pygame.draw.circle(scr, BLACK, (item[1] * 100 + 50, item[0] * 100 + 50), 30, 3)


def draw_cross(scr: object, item: tuple) -> None:
    """
    Рисует крестики
    :param scr: экран pygame (Surface)
    :param item: кортеж с номером клетки игрового поля
    """
    draw_line(scr, (item[1] * 100 + 20, item[0] * 100 + 20), (item[1] * 100 + 80, item[0] * 100 + 80))
    draw_line(scr, (item[1] * 100 + 20, item[0] * 100 + 80), (item[1] * 100 + 80, item[0] * 100 + 20))


def draw_item(scr: object, item: tuple, item_type: int) -> None:
    """

    :param scr: экран pygame (Surface)
    :param item: кортеж с номером клетки игрового поля
    :param item_type: 1 - игрок, 0 - компьютер
    """
    if item_type:
        draw_cross(scr, item)
    else:
        draw_zero(scr, item)


def draw_line(scr: object, a: tuple, b: tuple) -> None:
    """
    Рисует линию для игрового поля
    :param scr: экран pygame (Surface)
    :param a: кортеж с координатами точки а
    :param b: кортеж с координатами точки b
    """
    pygame.draw.line(scr, BLACK, a, b, 3)


def draw_field(scr: object) -> None:
    """
    Рисует игровое поле
    :param scr: экран pygame (Surface)
    """
    draw_line(scr, (0, 100), (300, 100))
    draw_line(scr, (0, 200), (300, 200))
    draw_line(scr, (100, 0), (100, 300))
    draw_line(scr, (200, 0), (200, 300))


def next_player(player_num: int) -> int:
    """
    Переключает ход на следующего игрока.
    В текущей реализации функция не используется.
    Была сделана до того, как в игру добавился бот
    :param player_num: номер предыдущего игрока
    :return: номер следующего игрока
    """
    return 0 if player_num else 1


def restart(scr: object, fnt: object) -> None:
    """
    Функция для запуска повторной игры.
    Очищает игровое поле, перерисовывает его и перезапускает игру.
    Также используется при первоначальной инициализации перед основным циклом игры.
    :param scr: экран pygame (Surface)
    :param fnt: шрифт pygame
    """
    global field
    global game_over
    game_over = False
    field = [['', '', ''] for _ in range(3)]
    scr.fill(BLUE)
    draw_field(scr)
    text_player = fnt.render("Игрок: X - крестики", False, BLACK)
    text_bot = fnt.render("Компьютер: O - нолики", False, BLACK)
    text_restart = f1.render("Начать сначала", False, BLACK)
    pygame.draw.polygon(screen, BLACK, [(10, 400), (10, 450), (185, 450), (185, 400)], 3)
    scr.blit(text_player, (10, 310))
    scr.blit(text_bot, (10, 340))
    scr.blit(text_restart, (20, 405))


def check_lines(cur_field: list, sign: str) -> bool:
    """
    Проверяет, есть ли зачеркнутые строки в игровом поле
    :param sign: X или O
    :param cur_field: матрица игрового поля
    :return: bool - зачеркивается линия или нет
    """
    for line in cur_field:
        if line[0] == line[1] == line[2] == sign:
            return True
    return False


def check_columns(cur_field: list, sign: str) -> bool:
    """
    Проверяет, есть ли зачеркнутые столбца в игровом поле
    :param sign: X или O
    :param cur_field: матрица игрового поля
    :return: bool
    """
    line1 = cur_field[0]
    line2 = cur_field[1]
    line3 = cur_field[2]
    for i in range(3):
        if line1[i] == line2[i] == line3[i] == sign:
            return True
    return False


def check_diagonal(cur_field: list, sign: str) -> bool:
    """
    Проверяет, есть ли зачеркнутые диагонали в игровом поле
    :param sign: X или O
    :param cur_field: матрица игрового поля
    :return:
    """
    line1 = cur_field[0]
    line2 = cur_field[1]
    line3 = cur_field[2]
    if line2[1] == sign and (line1[0] == line2[1] == line3[2] or line1[2] == line2[1] == line3[0]):
        return True
    else:
        return False


def is_win(cur_field: list, sign: str) -> bool:
    """
    Проверяет, выиграл ли игрок
    :param sign: X или O
    :param cur_field: матрица игрового поля
    :return:
    """
    lines_result = check_lines(cur_field, sign)
    if lines_result:
        return True
    columns_result = check_columns(cur_field, sign)
    if columns_result:
        return True
    diagonal_result = check_diagonal(cur_field, sign)
    if diagonal_result:
        return True
    return False


def is_dead_heat(cur_field: list) -> bool:
    """
    Функция для проверки ничьи.
    :param cur_field: матрица игрового поля
    :return: True - ничья, не осталось свободных клеток
    """
    dead_heat_flag = True
    for i in range(len(cur_field)):
        for j in range(len(cur_field)):
            if cur_field[i][j] == "":
                dead_heat_flag = False
                break
    return dead_heat_flag


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Крестики-нолики")

screen.fill(GREEN)
# инициализация шрифта для вывода текста
f1 = pygame.font.SysFont('arial', 24)

# инициализация матрицы игрового поля
field = [['', '', ''] for _ in range(3)]

pygame.display.flip()
# Цикл игры
mainloop = True
player = 1
BOT = 0
restart(screen, f1)

game_over = False
while mainloop:
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            mainloop = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # если нажата мышка, берем позицию
            mouse_pos = pygame.mouse.get_pos()
            if mouse_pos[0] <= 300 and mouse_pos[1] <= 300 and not game_over:
                # если кликнули мышью в область игрового поля и игра еще не завершена
                # фиксируем ход игрока, рисуем клетку, проверяем на победу, ходит компьютер
                item_x = mouse_pos[1] // 100
                item_y = mouse_pos[0] // 100
                if field[item_x][item_y] == "":
                    field[item_x][item_y] = "X" if player else "O"
                    draw_item(screen, (item_x, item_y), player)
                    if not is_win(field, "X"):
                        if not is_dead_heat(field):
                            x, y = random.randint(0, 2), random.randint(0, 2)
                            while field[x][y] != "":
                                x, y = random.randint(0, 2), random.randint(0, 2)
                            field[x][y] = "O"
                            draw_item(screen, (x, y), BOT)
                            if is_win(field, "O"):
                                game_over = True
                                text_comp_win = f1.render("Победил компьютер!", False, BLACK)
                                screen.blit(text_comp_win, (10, 460))
                        else:
                            dead_heat = f1.render("Ничья!", False, BLACK)
                            screen.blit(dead_heat, (10, 460))

                    else:
                        game_over = True
                        text_player_win = f1.render("Вы победили! Поздравляем!", False, BLACK)
                        screen.blit(text_player_win, (10, 460))

                else:
                    print("Сообщение - клетка уже занята")
            elif 10 < mouse_pos[0] < 185 and 400 < mouse_pos[1] < 450:
                # Если нажали в область кнопки 'Начать сначала' перезапускаем игру
                restart(screen, f1)

    pygame.display.update()

pygame.quit()

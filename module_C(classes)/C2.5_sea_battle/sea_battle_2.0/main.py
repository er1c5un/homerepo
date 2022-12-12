import pygame
from objects import Board, User, AI, Game

# количество попыток разместить корабли на досках
count_of_tries = 0

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Морской бой")

#screen.fill(GREEN)
# инициализация шрифта для вывода текста
f1 = pygame.font.SysFont('arial', 24)
clock = pygame.time.Clock()
pygame.display.flip()

while True:
    try:
        my_board = Board(hide=False)
        ai_board = Board(hide=True)
        player = User(mine_board=my_board, enemy_board=ai_board)
        ai = AI(mine_board=ai_board, enemy_board=my_board)
        game = Game(player, my_board, ai, ai_board)
        game.place_ships(my_board, player)
        game.place_ships(ai_board, ai)
        break
    except ValueError:
        pass

    if count_of_tries > 10:
        raise ValueError('Не удалось проинициализровать доску, 1000 попыток')
    else:
        count_of_tries += 1

game.start(screen, f1, clock)

pygame.quit()
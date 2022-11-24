def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def quadratic_solve(a, b, c):
    dis = discriminant(a, b, c)
    if dis < 0:
        return 'Нет вещественных корней'
    elif dis == 0:
        return -b / (2 * a)
    else:
        return (-b - dis ** 0.5) / (2 * a), (-b + dis ** 0.5) / (2 * a)

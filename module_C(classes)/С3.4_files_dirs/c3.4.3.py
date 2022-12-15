import os

dir = input("Введите полный путь:")
start_dir = dir if dir else os.getcwd()

for root, dirs, files in os.walk(start_dir):
    print("Текущая директория", root)
    print("---")

    if dirs:
        print("Список папок", dirs)
    else:
        print("Папок нет")
    print("---")

    if files:
        print("Список файлов", files)
    else:
        print("Файлов нет")
    print("---")

    if files and dirs:
        print("Все пути:")
    for f in files:
        print("Файл ", os.path.join(root, f))
    for d in dirs:
        print("Папка ", os.path.join(root, d))
    print("===")
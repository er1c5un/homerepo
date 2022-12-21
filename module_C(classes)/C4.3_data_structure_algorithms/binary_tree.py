class BTree:
    def __init__(self, value=0):
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, next_value):
        if self.left_child is None:
            self.left_child = BTree(next_value)
        else:
            new_left_child = BTree(next_value)
            new_left_child.left_child = self.left_child
            self.left_child = new_left_child
        return self

    def insert_right(self, next_value):
        if self.right_child is None:
            self.right_child = BTree(next_value)
        else:
            new_right_child = BTree(next_value)
            new_right_child.left_child = self.right_child
            self.right_child = new_right_child
        return self

    def pre_order(self):
        print(self.value)  # процедура обработки

        if self.left_child is not None:  # если левый потомок существует
            self.left_child.pre_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.pre_order()  # рекурсивно вызываем функцию

    def post_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.post_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.post_order()  # рекурсивно вызываем функцию

        print(self.value, end=', ')

    #инфиксный способ обхода в глубину
    #читаем дерево слева направо
    #сначала шагаем в левого потомка каждый раз, затем печатаем текущий узел,
    #и только потом идем в правого потомка
    def in_order(self):
        if self.left_child is not None:  # если левый потомок существует
            self.left_child.in_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

        if self.right_child is not None:  # если правый потомок существует
            self.right_child.in_order()  # рекурсивно вызываем функцию

a = BTree(2).insert_left(7).insert_right(5)
node_7 = a.left_child.insert_left(2).insert_right(6)
node_6 = node_7.right_child.insert_left(5).insert_right(11)
node_5 = a.right_child.insert_right(9)
node_9 = node_5.right_child.insert_left(4)
a.post_order()
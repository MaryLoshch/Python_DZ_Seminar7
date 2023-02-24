# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод:
# print_operation_table(lambda x, y: x * y)
# Вывод:
#  1 2 3 4 5 6
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36

num_rows = int(input('Ввести кол-во строк: '))
num_columns = int(input('Ввести кол-во столбцов: '))
operation = input(
    'Выберите операцию сумма(sum), умножение(mult), вычитание(min) или деление(div): ')


if operation == 'sum' or operation == 'сумма':
    def operation(x, y): return x + y - 2
elif operation == "mult" or operation == 'умножение':
    def operation(x, y): return x * y
elif operation == 'min' or operation == 'вычитание':
    def operation(x, y): return x - y
elif operation == 'div' or operation == 'деление':
    def operation(x, y): return x / y
else:
    print('Ошибка ввода ')


def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        new_list = []
        for j in range(1, num_columns + 1):
            new_list.append(str(operation(i, j)))
        print("\t".join(new_list))


print_operation_table(operation, num_rows, num_columns)


# задача 1-1
# Ввести два числа x и y.
# Напечатать сумму и произведение этих чисел
print("задача 1-1")
x = float(input("введите значение x = "))
y = float(input("введите значение y = "))
print(f'сумма x и y = {x} + {y} = {x + y}')
print(f'произведение x и y = {x} * {y} = {x*y}')

# задача 1-2
# Ввести два числа x и y.
# Напечатать наибольшее из чисел
# x + y, x y, x*y, x/y, x//y
print("задача 1-2")
x = float(input("введите значение x = "))
y = float(input("введите значение y = "))

a = x + y
print("+ ", a)

b = x - y
print("- ", b)

c = x * y
print("* ", c)

# деления на 0
if y == 0:
    d = None
    f = None
    print("/ - ноль в знаменателе ", d)
    print("// - ноль в знаменателе ", f)
    list_1 = [a, b, c] #создание списка чисел
else:
    d = x / y
    print("/ ", d)
    f = x // y
    print("// ", f)
    list_1 = [a, b, c, d, f] #создание списка всех имеющихся чисел

max_num = max(list_1) #поиск максимального значения из списка
print("Наибольшее из чисел: ", max_num)

# задача 1-3
# Ввести два числа x и y.
# Напечатать ВТОРОЕ ПО ВЕЛИЧИНЕ из чисел
# x + y, x y, x*y, x/y, x//y
print("задача 1-3")
list_1.remove(max_num) #удаление максимального значения из списка
second_max_num = max(list_1) #поиск второго максимального значения из списка
print("Второе по величине число: ", second_max_num)

#конец
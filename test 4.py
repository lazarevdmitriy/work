# Напишите программу, которая запрашивает два
# целых числа x и y, после чего вычисляет и выводит
# значение x в степени y.

x = int(input("Введите целое число x: "))
y = int(input("Введите целое число y: "))

result = x ** y

print(f"{x} в степени {y} равно {result}")

# Подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры.

count = 0

for num in range(100, 1000):
    num_str = str(num)
    if num_str[0] == num_str[1] or num_str[1] == num_str[2] or num_str[0] == num_str[2]:
        count += 1

# print(f"Количество целых чисел в диапазоне от 100 до 999 с двумя одинаковыми цифрами: {count}")

# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.

count = 0

for num in range(100, 10000):
    num_str = str(num)
    if len(set(num_str)) == len(num_str):
        count += 1

# print(f"Количество целых чисел в диапазоне от 100 до 9999 с различными цифрами: {count}")

# Пользователь вводит любое целое число. Необходимо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.

num = input("Введите целое число: ")
result = ""

for digit in num:
    if digit not in ['3', '6']:
        result += digit

print(f"Число без цифр 3 и 6: {result}")
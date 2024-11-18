n = int(input('Введите число с ворот: '))
dividers_list = []
res = []

for i in range(3, n + 1):   # Тут создаем список делителей введенного числа
    if n % i == 0:
        dividers_list.append(i)

number = 1  # Первое число пары. Оно всегда меньше n / 2
while number < n / 2:
    for divider in dividers_list:
        if number < divider / 2:
            res.append(str(number))
            res.append(str(divider - number))
        else:
            continue
    number += 1

print(f'Ваш пароль: {''.join(res)}')
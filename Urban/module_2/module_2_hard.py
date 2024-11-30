n = int(input('Введите число с ворот: '))
res = []

for number in range(1, int((n + 1) / 2)):   # Создаем первое числа пары
    for divider in range(3, n + 1):    # Цикл для делителей числа
        if n % divider == 0 and number < divider / 2:
            res.append(str(number))
            res.append(str(divider - number))

print(f"Ваш пароль: {''.join(res)}")

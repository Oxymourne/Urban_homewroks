numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []

''' Тут внесу немного ясности в циклы. Элементы перебираю в срезе numbers, чтобы исключить 1
Флаг засунул в первый цикл, чтобы при его изменении он автоматически становился True, когда берем новый элемент
Также использовал break, как было в не обязательном пункте
Вывод сделал через f-строки и тройные кавычки, чтобы сохранился формат
'''

for i in numbers[1::]:
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime is True:
        primes.append(i)
    else:
        not_primes.append(i)

print(f'''Primes: {primes}
Not Primes: {not_primes}''')

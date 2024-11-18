n = int(input('Введите число с ворот: '))
dividers_list = []
res = []

for i in range(3, n + 1):
    if n % i == 0:
        dividers_list.append(i)

print(dividers_list)

number = 1
while number < n / 2:
    for j in dividers_list:
        if number > j // 2:
            continue
        res.append(str(number))
        res.append(str(j - number))
    number += 1

print(''.join(res))
print('13141911923282183731746416515614713812911')
print('13141911923282183731746416515614713812911' == ''.join(res))

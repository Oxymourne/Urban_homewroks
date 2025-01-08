# Используем %
team1_name = input('Введите название команды 1: ')
team1_num = int(input('Введите количество участников команды "%s": ' % team1_name))

print('В команде "%s" %s участников' % (team1_name, team1_num))
print()

team2_name = input('Введите название команды 2: ')
team2_num = int(input('Введите количество участников команды "%s": ' % team2_name))

print('В команде "%s" %s участников' % (team2_name, team2_num))
print()
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))
print('-' * 30, end='\n')

# Используем format()
score_1 = int(input('Сколько задач решила команда "{}": '.format(team1_name)))
team1_time = float(input('За какое время команда "{}" выполнила задание: '.format(team1_name)))
print()
score_2 = int(input('Сколько задач решила команда "{}": '.format(team2_name)))
team2_time = float(input('За какое время команда "{}" выполнила задание: '.format(team2_name)))
print()
print('Команда "{}" решила {} задач за {} с'.format(team1_name, score_1, team1_time))
print('Команда "{}" решила {} задач за {} с'.format(team2_name, score_2, team2_time))
print('-' * 30, end='\n')

# Используем f-строки
print(f'Команды решили {score_1} и {score_2} задач')

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time) / tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'победа команды {team1_name}!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'победа команды {team2_name}!'
else:
    result = 'ничья!'

print(f'Результат битвы: {result}')
print()
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

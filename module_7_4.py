# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2


if score_1 > score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'


team1_str = "В команде Мастера кода участников: %d !" % team1_num
print(team1_str)

teams_str = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(teams_str)

score2_str = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(score2_str)

time2_str = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(time2_str)

score_str = f"Команды решили {score_1} и {score_2} задач."
print(score_str)

result_str = f"Результат битвы: {challenge_result}"
print(result_str)

tasks_str = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!"
print(tasks_str)

from random import randint
import csv
from pprint import pprint

# 1. Создать csv файл с данными следующей структуры: Имя, Фамилия, Возраст.
# Создать отчетный файл с информацией по количеству людей входящих в ту или иную
# возрастную группу. Возрастные группы: 1-12, 13-18, 19-25, 26-40, 40+.
firstnames = ['ivan', 'slava', 'ulia', 'jenya', 'denis', 'igor',
              'muslim', 'radik', 'natasha', 'vlad', 'jacks', 'ulia', 'petya', 'andrew', 'alice']
secondnames = ['petrov', 'usatov', 'polisatov', 'hvastunov', 'nosatov', 'dzevadze', 'shushkupa', 'ugvey']

people = [[firstnames[randint(0, len(firstnames) - 1)],
           secondnames[randint(0, len(secondnames) - 1)],
           str(randint(0, 50))] for _ in range(30)]

# без либы
# with open('people.csv','a') as f:
#     for p in people:
#         f.writelines(','.join(p) + '\n')

# c либой
# with open('people.csv', 'a', newline='') as csvfile:
#     humanwriter = csv.writer(csvfile)
#     for p in people:
#         humanwriter.writerow(p)


with open('people.csv', 'r', newline='') as csvfile:
    people_ages_groups = {
        (1, 12): 0,
        (13, 18): 0,
        (19, 25): 0,
        (26, 40): 0,
        (40, 100): 0
    }
    humanreader = csv.reader(csvfile)
    # люди с 15 годами возраста находятся на индексе 14 .example
    people_ages_list = [0 for age in range(1, 51)]

    for row in humanreader:
        people_age = int(row[2])
        people_ages_list[people_age - 1] += 1

        # people.append(row)

    for age_group_interval, count in people_ages_groups.items():
        for age in range(age_group_interval[0], age_group_interval[1] + 1):
            age_index = age - 1
            if age_index > len(people_ages_list) - 1:
                break
            people_ages_groups[age_group_interval] += people_ages_list[age_index]

    print(people_ages_groups)
# 2. Создать csv файл с данными о ежедневной погоде.
# Структура: Дата, Место, Градусы, Скорость ветра.
# Найти среднюю погоду(скорость ветра и градусы) для Минска за последние 7 дней.


# 3. Дан файл, содержащий различные даты. Каждая дата - это число, месяц и год.
# Найти самую раннюю дату.

from random import randint
import csv
from pprint import pprint
from datetime import date, timedelta

today = date.today()

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

#
# with open('people.csv', 'r', newline='') as csvfile:
#     people_ages_groups = {
#         (1, 12): 0,
#         (13, 18): 0,
#         (19, 25): 0,
#         (26, 40): 0,
#         (40, 100): 0
#     }
#     humanreader = csv.reader(csvfile)
#     # люди с 15 годами возраста находятся на индексе 14 .example
#     people_ages_list = [0 for age in range(1, 51)]
#
#     for row in humanreader:
#         people_age = int(row[2])
#         people_ages_list[people_age - 1] += 1
#
#         # people.append(row)
#
#     for age_group_interval, count in people_ages_groups.items():
#         for age in range(age_group_interval[0], age_group_interval[1] + 1):
#             age_index = age - 1
#             if age_index > len(people_ages_list) - 1:
#                 break
#             people_ages_groups[age_group_interval] += people_ages_list[age_index]
#


# 2. Создать csv файл с данными о ежедневной погоде.
# Структура: Дата, Место, Градусы, Скорость ветра.
# Найти среднюю погоду(скорость ветра и градусы) для Минска за последние 7 дней.

people = [[firstnames[randint(0, len(firstnames) - 1)],
           secondnames[randint(0, len(secondnames) - 1)],
           str(randint(0, 50))] for _ in range(30)]

cities = 'Moscow', 'London', 'Washington', 'Minsk'
degrees_interval = (15, 26)
wind_speed_interval = (1, 10)
dates = ('20.05.2025', '03.06.2025')
weather_value = []
for day_num in range(10):
    day_date = date.today() - timedelta(days=day_num)
    weather_value.append([
        [
            day_date.isoformat(),
            city_name,
            randint(degrees_interval[0], degrees_interval[1]),
            randint(wind_speed_interval[0], wind_speed_interval[1])
        ]
        for city_name in cities
    ])
# создание файла погоды
# with open('weather.csv', 'a', newline='') as csvfile:
#     weather_observer = csv.writer(csvfile)
#     for day_info in weather_value:
#         weather_observer.writerow(day_info)

with open('weather.csv', 'r', newline='') as csvfile:
    weather_reader = csv.reader(csvfile)
    minsk_wind = []
    minks_degrees = []
    day_counter = 7
    while day_counter > 1:
        day_weather_info = next(weather_reader)
        minks_degrees.append(int(day_weather_info[3][2]))
        minsk_wind.append(int(day_weather_info[3][3]))
        day_counter -= 1
    middle_degrees = sum(minks_degrees) // len(minks_degrees)
    middle_wind = sum(minsk_wind) // len(minsk_wind)

    print(f'Minsk last 7 days middle weather is {middle_degrees} as degrees and {middle_wind} as wind')

    # 3. Дан файл, содержащий различные даты. Каждая дата - это число, месяц и год.
    # Найти самую раннюю дату.

with open('dates.csv','r',newline='') as csvfile:
    dates_reader = csv.reader(csvfile)
    earliest_date = False
    for row_date in dates_reader:
        if earliest_date is False:
           earliest_date = row_date
           continue
        if row_date < earliest_date:
            earliest_date = row_date
    print(earliest_date)


import collections
import random


def rand_func(number, *args):
    lst = []
    for n in range(0, number, 1):
        lst.append(random.choice(args))
    return lst

# может быть несколько наиболее редко встречающихся первыъх букв в именах
def most_rare_start_letter(names_list):
    letters_list = list(map(lambda x: x[0], names_list))
    letters_count = collections.Counter(letters_list).items()
    min_count = min(letters_count, key=lambda x: x[1])
    most_rare = [x[0] for x in letters_count if x[1] == min_count[1]]
    return most_rare

# может быть несколько наиболее часто встречающихся имён
def most_common_name(names_list):
    names_count = list(collections.Counter(names_list).items())
    max_count = max(names_count, key=lambda x: x[1])
    most_common = [x[0] for x in names_count if x[1] == max_count[1]]
    return most_common


names_list = [
    'Геральт из Ривии',
    'Йенифер из Венгерберга',
    'Трисс Меригольд из Марибора',
    'Золтан Хивай',
    'Цирилла',
    'Каланте',
    'Эйст Турсеах',
    'Крах Ан Крайт',
    'Эмиель Регис',
    'Эмгыр Вар Эмрейс',
    'Высогота из Корво',
    'Вильгефорц из Роггевеена',
    'Доррегарай из Волле',
    'Мильва',
    'Лютик',
    'Весемир',
    'Филиппа Эйльхарт',
    'Шеала Де Тансервилль',
    'Ассирэ вар Анагыд',
    'Мышовур',
    'Дийкстра'
]

rand_list = rand_func(100, *names_list)

print("Counter из модуля collections для операций на списке слов")

print()
print("Список имён с количеством в списке-источнике:")
c = collections.Counter(rand_list)
for i in c.most_common():
    print(f'{i[0]}.....{i[1]}')

print()
print("Самое часто встречающееся имя через метод most_common:")
print(c.most_common(1)[0][0])
print("Самое часто встречающееся имя через пользовательский метод:")
print(most_common_name(rand_list))


print()
print('Список первых букв в словах из списка-источника')
start_letter = collections.Counter(list(map(lambda x: x[0].lower(), rand_list)))
for i in start_letter.items():
    print(f'{i[0]}......{i[1]}')

print()
print("Наименее редко встречающаяся первая буква в именах из списка-источника через метод most_common")
print(start_letter.most_common()[-1][0])
print("Наименее редко встречающаяся первая буква в именах из списка-источника через пользовательский метод")
print(most_rare_start_letter(rand_list))

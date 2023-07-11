# Создайте словарь со списком вещей для похода в качестве ключа и их массой в
# качестве значения. Определите какие вещи влезут в рюкзак передав его
# максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.

import random

a = {"Вода": 55, "Палатка": 35, "Хлеб": 25, "Мясо": 30, "Розжиг": 15, "Овощи": 20, "Сок": 30}

maximum_load = 90
counter = 0
List_artibute = []
while counter < maximum_load:
    key, value = random.choice(list(a.items()))
    if key in List_artibute:
        continue
    if counter + value > maximum_load:
        break
    counter += value
    List_artibute += (str(key), str(value))

print(List_artibute, "=", counter)
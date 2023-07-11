# Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

dict_frends_atribute = {"Иван": ("Сок", "Хлеб", "Овощи"),\
                        "Михаил": ("Топор", "Хлеб", "Пила"),\
                        "Максим": ("Мясо", "Палатка", "Спички")}

def list_atribute_frends(dict_list):
    list_atribute = []
    for atribut in dict_list.values():
        list_atribute += atribut
    return list_atribute

count = 0
count += 1

def dict_unicum_atribute (dict_list):
    name_not_atribute = []
    new_dict = {}
    count = 0
    for key, value in dict_frends_atribute.items():
        name_not_atribute.append(key)
        new_dict[key] = []
        for j in value:
            for k in list_atribute_frends(dict_frends_atribute):
                if k == j:
                    count += 1
            if count == 1:
                new_dict[key] += [j]
            if count > 1:
                name_not_atribute.remove(key)
            count = 0
    print("Человек, у которого вещи не дублируются остальными: ", name_not_atribute)
    return new_dict

print(f"Вещи которые взяли все три друга: {list_atribute_frends(dict_frends_atribute)}")
print(f"Уникальные вещи, которые взял каждый друг:  {dict_unicum_atribute(dict_frends_atribute)}")
# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

list = [8, 2, 3, 3, 4, 8, 5, 4, 5, 10, 12]
print("Список: ", list)
duplicate = []

for item in list:
    if list.count(item) > 1 and item not in duplicate:
        duplicate.append(item)

print("Повторяющиеся элементы в списке:", duplicate)
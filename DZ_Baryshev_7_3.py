# Задание 1
list1 = [3, 7, 1, 9]
list2 = [4, 2, 8, 5]
list3 = [6, 10, 12, 11]
list4 = [15, 13, 14, 16]
list_sum = list1 + list2 + list3 + list4
sort_type = input("Введите '1' для сортировки по возрастанию или '2' для сортировки по убыванию: ")
if sort_type == "1":
    list_sum.sort()
elif sort_type == "2":
    list_sum.sort(reverse=True)
else:
    print("Некорректный ввод")
print("Отсортированный список:", list_sum)
search_value = int(input("Введите значение для поиска: "))
found = False
for i in range(len(list_sum)):
    if list_sum[i] == search_value:
        print(f"Значение {search_value} найдено на позиции {i}")
        found = True
        break
if not found:
    print(f"Значение {search_value} не найдено в списке")

# Задание 2
list1 = [3, 7, 1, 9]
list2 = [4, 2, 8, 5]
list3 = [6, 10, 12, 11]
list4 = [15, 13, 14, 16]
com_list = list(set(list1 + list2 + list3 + list4))
sort_type = input("Введите '1' для сортировки по возрастанию или '2' для сортировки по убыванию: ")
if sort_type == "1":
    com_list.sort()
elif sort_type == "2":
    com_list.sort(reverse=True)
else:
    print("Некорректный ввод")
print("Отсортированный список уникальных элементов:", com_list)
search_value = int(input("Введите значение для поиска: "))


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1


result = binary_search(com_list, search_value)
if result != -1:
    print(f"Значение {search_value} найдено на позиции {result}")
else:
    print(f"Значение {search_value} не найдено в списке")

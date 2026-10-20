# lst.reverse()
# print(lst)

# lst1 = [12,15,16,17,5]
# lst2 = [1,2,3]
# lst1.append([2,12,15])
# print(lst1)
# print(lst1[-1][0])

# lst1.extend(lst2)
# print(lst1)  

# new_lst = lst1 + lst2
# print(new_lst)

# #copy

# a = [1,2,3]
# b = a
# c = a.copy()

# a[1]=7

# print(a)
# print(b)
# print(c)

# list_ss = [1,2,3,4,5]
# print(list_ss.insert(0,5))
# print(list_ss.append(6))
# print(list_ss)
# # print(list_ss.clear())
# print(list_ss.count(6))
# print(list_ss.pop(0))
# list_ss.pop(-1)
# lol = list_ss.index(2)
# print(lol)
# print(max (list_ss))
# print(min (list_ss))




# my_list = [10, 20, 30, 40, 50]
# my_list.insert(0, 5)  # [5, 10, 20, 30, 40, 50]
# my_list.append(60)  # [5, 10, 20, 30, 40, 50, 60]
# print("Список:", my_list)
# count_elements = len(my_list)
# print("Количество элементов:", count_elements)
# is_empty = len(my_list) == 0  
# print("Список пустой?", is_empty)
# my_list.pop(0)  
# my_list.pop()  

# value_to_find = 30
# if value_to_find in my_list:
#   index_of_value = my_list.index(value_to_find)
#   print(f"Элемент {value_to_find} найден на индексе: {index_of_value}")
# else:
#   print(f"Элемент {value_to_find} не найден")


# min_val = min(my_list)
# max_val = max(my_list)
# print("Наименьшее значение:", min_val)
# print("Наибольшее значение:", max_val)

# my_list.clear()  # или my_list = []
# print("Список после очистки:", my_list)

# year = 2026
# date = '15-10-20226'
# print("Это год:",year,"дата:",date)
# print("Это год:",year,"дата:"+date)
# print(f"Это год: {year} дата: {date}")

# rg = range(0,5)
# print (list(rg))

# for i in range(0,5):
#     print(i)

# for i in range(5):
#     print("hello")

# for x in range(0,10,1): #[0:10:1]
#     print(x)

# student = ["Name1", 'Name2', 'Name3', 'Name4']
# group = ['ITB28', 'ITB27']

# for st in student:
#     print(st)

# for i in group:
#     for j in student:
#         print(j, i)

# Напишите функцию для преобразования имени в инициалы. 
# Это задание строго принимает два слова, разделённых одним пробелом.
# В результате должны быть выведены две заглавные буквы, разделённые точкой.
# Это должно выглядеть примерно так:
# Sam Harris=>S.H
# patrick feeney=>P.F

# def abbrev_name(name):
#   first, last = name.split()
#   return f"{first[0].upper()}.{last[0].upper()}"

# Напишите код на питоне(не функцию) для преобразования имени в инициалы. 
# Это задание строго принимает два слова, разделённых одним пробелом.
# В результате должны быть выведены две заглавные буквы, разделённые точкой.
# Это должно выглядеть примерно так:
# Sam Harris=>S.H
# patrick feeney=>P.F

# fio = input().upper().split()
# print(fio)
# print(f"{fio[0][0]}. {fio[1][0]}")

# for i in range(4):
#     for j in range(4):
#         print("*", end='')
#     print()


for i in range(1, 6):
    print("*" * i)
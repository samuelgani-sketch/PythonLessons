#i = input()
# print (i.isalpha())
# print (i.islower())
# print (i.isupper())
# print (i.isdigit())
# print (i.isnumeric())
# print (i.startswith("heoo"))
# print (i.endswith("koi"))
# print (i.lower())
# print (i.upper())
# print (i.title())
# print (i.capitalize())
# print (i.strip())
# print (i.lstrip())
# print (i.rstrip())
#print (i.find("O"))
#print (i.find("O", 5))
#print (i.find("O", 4,5))

# phone_num ='+996 123 456'
# # phone_num =phone_num.replace("+", "-")
# # phone_num =phone_num.replace("+", " ")
# phone_num =phone_num.replace(" ", "-", 1)
# print(phone_num)

# word = "Hello nether"
# print(word.replace("nether", "world"))

###split
# st="In a distant, but not so unrealistic, future"
# print(st.split(',',))
# st= ["owrueioroi", 'cmewp', '?']
# print(" ".join(st))

# st="In a distant, but not so unrealistic, future"
# st_split = st.split()
# print(st_split)
# st_sorted =(sorted(st_split, key=len))
# print(st_sorted)

# st_new = " ".join(st_sorted)
# print(st_new)
# print(type(st_new))

###if/elif/else

# grade = input("Enter grade: ")

# if grade == "5":
#     print("Молодец, так держать!")
# elif grade == "4":
#     print("Аххх! Еще чуть-чуть и ты отличник!")
# elif grade == "3":
#     print("Старайся учиться еще лучше!")
# else:
#     print("Ну! Ты можешь лучше учиться, я в этом уверен!")

# score = float(input("Введите баллы: "))

# if score < 25:
#     grade = "F"
# elif score <= 45:
#     grade = "E"
# elif score <= 50:
#     grade = "D"
# elif score <= 60:
#     grade = "C"
# elif score <= 80:
#     grade = "B"
# else:
#     grade = "A"

# print("Ваша оценка:", grade)

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))

# result = (a % 2 == 0) and (b % 2 == 0)
# print(result) 



def calculate():
    try:
        a = float(input("Первое число: "))
    except ValueError:
        print("Ошибка: введите корректное число!")
        return

    op = input("Операция (+, -, *, /): ").strip()
    if op not in ("+", "-", "*", "/"):
        print("Ошибка: неизвестная операция!")
        return

    try:
        b = float(input("Второе число: "))
    except ValueError:
        print("Ошибка: введите корректное число!")
        return

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    else:
        if b == 0:
            print("Ошибка: деление на ноль!")
            return
        result = a / b

    def fmt(x):
        # Целые числа выводим без ".0"
        return int(x) if x == int(x) else x

    print(f"{fmt(a)} {op} {fmt(b)} = {fmt(result)}")


calculate()
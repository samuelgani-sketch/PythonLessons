#задача 1
data = input("Введите что-нибудь: ")
if data:
    print("ОК")


#задача 2
a = int(input("Ширина форточки, см: "))
b = int(input("Высота форточки, см: "))
d = int(input("Диаметр головы, см: "))

gap = 1  # зазор с каждой стороны, см

if d + 2 * gap <= a and d + 2 * gap <= b:
    print("Вася сможет высунуть голову")
else:
    print("Вася не сможет высунуть голову")


#задача 3
a = int(input())
b = int(input())
c = int(input())

print("Максимум:", max(a, b, c))
print("Минимум:", min(a, b, c))

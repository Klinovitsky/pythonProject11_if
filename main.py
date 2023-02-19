# Netology if

name = input("Введите имя: ")
login = "Dima"

# Логический тип данных True\False
print(name == login)

if name == login:
    print("Hello", name)
elif len(name) < 3:
    print("The name is too short (condition elif < 1)")
# elif взаимоисключающие, как только встречается первое истинное выражение, все оставшееся не выполняется
elif len(name) == 2:
    print("The name is too short (condition elif = 2)")
else:
    z = 10//4
    print("Целочисленное деление. 10//2 =  ", z)

print("The end")

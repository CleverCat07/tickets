#Пользователь вводит число, программа должна вывести на экран его описание. Например, "положительное однозначное число", "отрицательное двухзначное" и т. п.

a = int(input("Enter a = "))

if a == 0:
    print("Нуль - однозначне число")
else:
    if a > 0:
        print("Додатнє")
    else:
        print("Від`ємне")

    if abs(a) < 10:
        print("Однозначне число")
    elif abs(a) < 100:
        print("Двохзначне число")
    else:
        print("Трьохзначне або більше число")
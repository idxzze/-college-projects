# 2. Даны два числа. Вывести порядковый номер меньшего из них.

try:
    a = int(input("Введите первое число: "))  # Запрашиваем ввод у пользователя
    b = int(input("Введите второе число: "))   # Запрашиваем ввод у пользователя

    # Находим порядковый номер меньшего числа
    if a < b:
        print("Порядковый номер меньшего числа:", 1)
    else:
        print("Порядковый номер меньшего числа:", 2)

except ValueError:
    print("Ошибка ввода")
except Exception:
    print("Произошла ошибка")
 
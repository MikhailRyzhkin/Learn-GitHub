numer1 = input("Введите первое число: ")
numer2 = input("Введите второе число: ")
if float(numer2) != 0:
    devided = float(numer1) / float(numer2)
    print("Результат деления одного числа на другое: ", devided)
else:
    print("Делить на ноль нельзя, получилась бесконечность")

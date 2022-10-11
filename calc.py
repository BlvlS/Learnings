def calc():
    try:
        a = int(input("Значение a:"))
        b = int(input("Значение b:"))
        print(a / b)
    except ZeroDivisionError:
        print("На 0 делить нельзя!")
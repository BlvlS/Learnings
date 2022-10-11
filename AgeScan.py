age = int(input("Укажите Свой Возраст."))
if (age >= 25):
    print("Можешь зайти сам!")
elif (age >= 18) and (age <25):
    print("Вход только с родителями!")
else:
    print("Подрасти Малыш!")

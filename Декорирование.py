def my_decor(func):
    def wrapper(n):
        print("strat")
        func(n)
        print("end")

    return wrapper


@my_decor
def my_func(number):
    print(number ** 2)



my_func(10)

import time

def my_decor(func):
    def my_wrapper():
        start_time = time.time()
        func()
        print(time.time() - start_time)
    return my_wrapper()

@my_decor
def spisok():
    sp = [i ** 2 for i in range(10) if i % 2 == 0]
    print(sp)

spisok
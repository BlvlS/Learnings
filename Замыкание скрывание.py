def message (x):
    def print_message(y):
        return x, y
    return print_message

d = message(4)
print(d(2))
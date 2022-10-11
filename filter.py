with open("123.txt") as f:
    n = int(f.readline())
    for i in range(n):
        a = list(map(int, f.readline().split()))
        b = list(filter(lambda x: (x % 2 != 0), (a)))
        print(b)
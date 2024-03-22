v = int(input())
for i in range(v):
    x, y = int(input()), int(input())

    print(x // y)
    print(x % y)

    if i < v - 1:
        print("")
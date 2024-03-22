def pattern(x, y, z):
    if x == 0 and y == 0:
        print(z)
    else:
        if y > 0:
            pattern(x - 1, y - 1, z + "1")
        if x > y:
            pattern(x - 1, y, z + "0")


v = int(input())
for i in range(v):
    x, y = input().split(" ")
    print("The bit patterns are")
    pattern(int(x), int(y), "")
    if i < v-1:
        print("") #dmoj :rolling_eyes:
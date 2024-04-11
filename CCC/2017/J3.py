a, b = (int(i) for i in input().split(" "))
c, d = (int(i) for i in input().split(" "))
t = int(input())

if (abs(a - c) + abs(b - d)) % 2 == t % 2 \
    and t >= abs(a - c) + abs(b - d):
    print("Y")
else:
    print("N")
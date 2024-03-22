# Throws a ValueError on the WCIPEG test cases, but I don't care cause it would've passed in CCC '96
for _ in range(int(input())):
    l, X, Y = int(input()), [int(i) for i in input().split(" ")], [int(i) for i in input().split(" ")]

    d = lambda i, j: j - i if j >= i and Y[j] >= X[i] else 0
    print(f"The maximum distance is {max([d(i, j) for j in range(l) for i in range(l)])}")
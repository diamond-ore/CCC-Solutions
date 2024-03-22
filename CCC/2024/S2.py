T, N = (int(i) for i in input().split(" "))
for i in range(T):
    v, o = list(input()), "T"
    for x in range(N - 1):
        a, b = v.count(v[x]), v.count(v[x + 1])
        if a == 1 == b or a != 1 != b:
            o = "F"
            break
    print(o)
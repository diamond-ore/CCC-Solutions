y = int(input())
for x in range(y):
    i, v = int(input()), 0
    u, o, e = i, 0, 0

    while True:
        print(f"Round {v}: {u} undefeated, {o} one-loss, {e} eliminated")
        if u == 1 and o == 1:
            u, o = 0, 2
        else:
            e, o, u = e + o // 2, o - o // 2 + u // 2, u - u // 2 
        v += 1
        if u == 0 and o == 1:
            break
    print(f"Round {v}: {u} undefeated, {o} one-loss, {e} eliminated")
    print(f"There are {v} rounds.")
    
    if x < y - 1:
        print("")
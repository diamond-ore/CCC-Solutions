for i in range(int(input())):
    subjects, verbs, objects = (lambda x, y, z: ([input() for _ in range(x)], [input() for _ in range(y)], [input() for _ in range(z)]))(int(input()), int(input()), int(input()))

    for i in subjects:
        for v in verbs:
            for g in objects:
                print(f"{i} {v} {g}.")
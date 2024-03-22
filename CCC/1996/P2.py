for _ in range(int(input())):
    n = int(input())
    x = n

    print(x)
    for _ in str(n):
        x = x if x == 11 else x // 10 - int(str(x)[-1])
        print(x)
        if x <= 11:
            break
    print(f"The number {n} is {'' if x == '11' else 'not '}divisible by 11.\n")

    '''
    # Lambda version:
    i = list(filter(lambda x: int(x) > 10, [x := str((int(x) // 10) - int(x[-1])) if int(x) > 10 else "0" for _ in x]))
    
    print(n)
    if len(i) > 0:
        print('\n'.join(i))
    print(f"The number {n} is {'' if x == '11' else 'not '}divisible by 11.\n")
    '''
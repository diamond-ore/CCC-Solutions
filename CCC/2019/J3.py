for _ in range(int(input())):
    line = input()
    string, last, quantity = "", line[0], 0
    for i in line:
        if i != last:
            string += f"{quantity} {last} "
            quantity = 0
        quantity += 1
        last = i
    string += f"{quantity} {last}"
    print(string)
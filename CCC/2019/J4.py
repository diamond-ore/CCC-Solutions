l = ['1', '2', '3', '4']

for c in input():
    c = c.lower()
    if c == "h":
        l[0], l[2] = l[2], l[0]
        l[1], l[3] = l[3], l[1]
    elif c == "v":
        l[0], l[1] = l[1], l[0]
        l[2], l[3] = l[3], l[2]

print(f"{l[0]} {l[1]}\n{l[2]} {l[3]}\n")
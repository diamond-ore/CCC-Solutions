o = input()
r = input()

n = set(o)
j = set(r)

safe = []
missing = []
bad = []

for i in n:
    if i in j:
        safe.append(i)
    elif i not in j:
        missing.append(i)

for i in j:
    if i not in safe:
        bad.append(i)

if len(missing) > 1:
    # quiet key
    if o.replace(missing[0], "").replace(missing[1], bad[0]) == r:
        print(missing[1], bad[0])
        print(missing[0])
    elif o.replace(missing[1], "").replace(missing[0], bad[0]) == r:
        print(missing[0], bad[0])
        print(missing[1])
else:
    # no quiet key
    print(missing[0], bad[0])
    print("-")
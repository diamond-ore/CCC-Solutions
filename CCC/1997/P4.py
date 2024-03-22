i, v = int(input()), 0
c, n = [' ' for _ in range(i)], ['' for _ in range(i)]
while v < i: # input loop
    x = input()
    if x == '':
        v += 1
    else:
        c[v] += x + ' \n '
        n[v] += x + ' '

for m in range(i): # output loop
    e, q = c[m], n[m].split(' ')[:-1]
    g = list(dict.fromkeys(q))
    for w in g:
        if q.count(w) > 1:
            k, t = " "+str(g.index(w) + 1)+" ", " "+w+" "
            e = e.replace(t, ' $ ', 1).replace(t, k).replace(t, k).replace(' $ ', t)
    print(e.replace(' \n ', '\n')[1:])
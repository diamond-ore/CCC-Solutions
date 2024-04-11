D = int(input())

sum = 0

for i in range(D % 720 + 1):
    h = [int(t) for t in str(i // 60 if i // 60 != 0 else 12)]
    m = [int(t) for t in f"{i % 60:0>2}"]
    s = ''.join(str(i) for i in h) + ''.join(str(i) for i in m)

    if m[1] - m[0] != 0:
        if ''.join(str(i) for i in range(h[0], m[1] + 1, m[1] - m[0])) == s:
            sum += 1
        elif ''.join(str(i) for i in range(h[0], m[1] - 1, m[1] - m[0])) == s:
            sum += 1
    elif len(set(s)) == 1:
        sum += 1

sum += 31 * (D // 720)

print(sum)
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline # speed glitch no clickbait

r, c = int(input()), int(input())

patch = [input() for _ in range(r)]
seen = [[False] * c for _ in range(r)]

total = 0
values = {"L":10, "M":5, "S":1}

def cluster(x, y):
    if x < 0 or x >= c or y < 0 or y >= r:
        return
    if seen[y][x] == True:
        return
    seen[y][x] = True
    slot = patch[y][x]
    if slot != '*':
        global total
        total += values[slot]
        cluster(x, y+1)
        cluster(x, y-1)
        cluster(x-1, y)
        cluster(x+1, y)

cluster(y=int(input()), x=int(input()))
print(total)
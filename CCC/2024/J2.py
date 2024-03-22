dusa_size = int(input())

while True:
    yobi_size = int(input())
    if dusa_size <= yobi_size:
        break
    dusa_size += yobi_size

print(dusa_size)
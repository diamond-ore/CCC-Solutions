team_a = int(input()) * 3 + int(input()) * 2 + int(input())
team_b = int(input()) * 3 + int(input()) * 2 + int(input())

print("T" if team_a == team_b else \
      "A" if team_a > team_b else "B")
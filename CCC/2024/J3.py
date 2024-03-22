n = int(input())
participants = [int(input()) for _ in range(n)]
scoreboard = sorted(set(participants), reverse=True)

print(scoreboard[2], participants.count(scoreboard[2]))
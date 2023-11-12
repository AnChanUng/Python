hour, min = map(int, input().split())
c = int(input())

hour = hour + c // 60
min = min + c % 60

if (min >= 60):
    min = min - 60
    hour = hour + 1

if (hour >= 24):
    hour = hour - 24

print(hour, min)

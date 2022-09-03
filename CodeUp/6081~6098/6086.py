# [CodeUp: 6086] [기초-종합] 거기까지! 이제 그만~

n = int(input())
i = 0
sum = 0

while True:
  sum += i
  i += 1
  if sum >= n:
    break
print(sum)
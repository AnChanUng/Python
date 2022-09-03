# [CodeUp: 6088] [기초-종합] 수 나열하기1

a, d, n = map(int, input().split())
result = a
for i in range(n-1):
  result += d
print(result)
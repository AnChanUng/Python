# [CodeUp: 6090] [기초-종합] 수 나열하기3

a, m, d, n = map(int, input().split())
result = a
for i in range(1, n):
    result = result * m + d
print(result)
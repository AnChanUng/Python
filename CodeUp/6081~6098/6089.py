# [CodeUp: 6089] [기초-종합] 수 나열하기2

a, r, n = map(int, input().split())
result = a
for i in range(0, n-1):
    result = result * r
print(result)
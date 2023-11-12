N, M = map(int, input().split())  # N:행의 개수, M: 열의 개수

result = 0

for i in range(N):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = 10001
#     for a in data:
#         min_value = min(min_value, a)
#     result = max(result, min_value)

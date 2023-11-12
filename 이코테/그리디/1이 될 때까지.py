N, K = map(int, input().split())
count = 0

# N이 K 이상이라면 K로 계속 나누기
while N >= K:
    while N % K != 0:  # n이 k로 나누어 떨어지지 않는다면
        N -= 1
        count += 1
    N //= K
    count += 1

# 마지막으로 남은 수에 대하여 1씩 빼기
while N > 1:
    N -= 1
    count += 1
print(count)

# while True:
#     target = (n // k) * k
#     count += (n - target)
#     n = target

#     if n < k:
#         break
#     count += 1
#     n //= k
# count += (n-1)
# print(count)

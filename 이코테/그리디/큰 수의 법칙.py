N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort()
first = data[N - 1]  # 가장 큰 수
second = data[N - 2]  # 두 번째로 큰 수

result = 0

while True:
    for i in range(K):  # 가장 큰 수를 K번 더하기
        if M == 0:  # m이 0이라면 반복문 탈출
            break
        result += first
        M -= 1  # 더할 때마다 1씩 빼기
    if M == 0:
        break
    result += second
    M -= 1

print(result)

# data.sort()
# first = data(n-1)
# second = data(n-2)

# count = int(m / (k+1)) * k
# count += m % (k+1)

# result = 0
# result += (count) * first
# result += (m-count) * second

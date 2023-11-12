N = int(input())

# n의 약수를 저장할 리스트 생성
divisors = []

# 1부터 N까지의 수 중 N의 약수를 찾아 리스트에 추가
for i in range(1, N+1):
    if N % i == 0:
        divisors.append(i)

# 약수를 오름차순으로 출력
print(" ".join(map(str, divisors)))

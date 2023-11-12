N, M = map(int, input().split())
data = list(map(int, input().split()))
array = [0] * 11  # 1부터 10까지의 무게를 담을 수 있는 리스트

for x in data:  # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1

count = 0

for i in range(1, M+1):   # 1부터 M까지 무게에 대하여 처리
    N -= array[i]         # 무게가 i인 볼링공의 개수 제외
    count += array[i] * N  # B가 선택하는 경우의 수와 곱하기

print(count)

# [백준 14720번] 우유축제 - (브론즈3, greedy)
# 딸기 -> 초코 -> 바나나 -> 딸기

N = int(input())
a = list(map(int, input().split()))
count = 0

for i in range(N):
    if a[i] == count % 3:
        count += 1

print(count)
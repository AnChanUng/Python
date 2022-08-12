# [백준 1546번] - 평균 - (브론즈1, 1차원배열)
import sys
input = sys.stdin.readline

N = int(input())
a = list(map(int,input().split()))
m = max(a)
sum = 0
for i in range(N):
    a[i] = a[i] / m * 100
    sum += a[i]
print(sum / N)
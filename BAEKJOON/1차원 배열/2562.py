# [백준 2562번] - 최대값 - (브론즈3, 1차원배열)
import sys
input = sys.stdin.readline

a = []

for i in range(9):
    N = int(input())
    a.append(N)

print(max(a))
print(a.index(max(a)) + 1)
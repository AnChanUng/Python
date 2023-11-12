import sys
input = sys.stdin.readline

N, M = map(int, input().split())

basekts = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for idx in range(i - 1, j):
        basekts[idx] = k

print(*basekts)

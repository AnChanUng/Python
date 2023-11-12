import sys
input = sys.stdin.readline

N, M = map(int, input().split())
box = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())
    temp = box[i-1]
    box[i-1] = box[j-1]
    box[j-1] = temp

for b in box:
    print(b, end=' ')

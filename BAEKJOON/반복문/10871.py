# [백준 10871번] - X보다 작은 수 - (브론즈5, 반복문)
import sys
input = sys.stdin.readline

N, X = map(int, input().split()) # N개로 이루어진 수열A와 정수 X
A = list(map(int, input().split()))

for i in range(N):
  if A[i] < X:
    print(A[i], end= " ")
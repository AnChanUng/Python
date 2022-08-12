# [백준 17608번] - 막대기 - (브론즈2, 스택)
import sys
input = sys.stdin.readline

N = int(input())               # 막대기의 개수
stack = []
count = 0

for i in range(N):
  h = int(input())
  while stack and stack[-1] <= h:
    stack.pop()
  stack.append(h)

count = len(stack)
print(count)
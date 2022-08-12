# [백준 15552번] - 빠른 A+B - (브론즈4, 반복문)
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
      A, B = map(int, input().split())
      print(A + B)
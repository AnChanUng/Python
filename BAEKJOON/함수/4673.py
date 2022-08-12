# [백준 4673번] - 셀프 넘버 - (실버5, 함수)
import sys
input = sys.stdin.readline

n = int(input())
a = n + n//10 + n%10

for i in range(n):
    print(a)
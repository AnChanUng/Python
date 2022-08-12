# [백준 2577번] - 숫자의 개수 - (브론즈2, 1차원배열)
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c))

for i in range(10):
    print(result.count(str(i)))
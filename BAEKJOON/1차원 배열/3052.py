# [백준 2577번] - 숫자의 개수 - (브론즈2, 1차원배열)
import sys
input = sys.stdin.readline

arr = []

for i in range(10):
    n = int(input())
    arr.append(n % 42)
    
arr = set(arr)
print(len(arr))
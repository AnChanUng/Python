# [백준 2588번] - 곱셈 - (브론즈3, 입출력과 사칙연산)
import sys
input = sys.stdin.readline

a = int(input())
b = int(input())

print(a*(b%10))
print(a*((b%100)//10))
print(a*(b//100))
print(a*b)
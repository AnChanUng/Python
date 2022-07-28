# [백준 1914번] - 하노이 탑 - (실버4, 스택)
import sys
input = sys.stdin.readline

def move(n, x, y):
    if n > 1:
        move(n - 1, x, 6 - x - y)
    
    print(x, y)

    if n > 1:
        move(n - 1, 6 - x - y, x)

n = int(input())
print(2**n - 1)

if n <= 20:
    move(n, 1, 3)
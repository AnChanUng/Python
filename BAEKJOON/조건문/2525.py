# [백준 2525번] - 오븐 시계 - (브론즈3, 조건문)

A, B = map(int, input().split()) #A:시간 B:분
C = int(input())                 #C:분

H = (A + ((B + C)//60)) % 24
M = (B + C) % 60
print(H, M)
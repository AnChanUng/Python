# [백준 5622번] - 다이얼
import sys
input = sys.stdin.readline

phone = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alphabet = list(input())
result = 0

for i in alphabet:
    for j in phone:
        if i in j:
            result += phone.index(j) + 3

print(result)
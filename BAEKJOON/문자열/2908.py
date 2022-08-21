# [백준 2908번] - 상수 - (브론즈2, 문자열)

A, B = input().split()

A = A[::-1]
B = B[::-1]
print(max(A, B))
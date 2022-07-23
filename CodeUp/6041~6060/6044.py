# [CodeUp: 6044] [기초-산술연산] 정수 2개 입력받아 자동 계산하기
# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 
# 자동으로 계산해보자. 단, b는 0이 아니다.

a, b = input().split()

print(int(a) + int(b))
print(int(a) - int(b))
print(int(a) * int(b))
print(int(a) // int(b))
print(int(a) % int(b))
print(format(int(a) / int(b), ".2f"))
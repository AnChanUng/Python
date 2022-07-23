# [CodeUp: 6064] [기초-3항연산] 정수 3개 입력받아 가장 작은 값 출력하기

a, b, c = map(int, input().split())

d = a if a < b else b
e = d if d < c else c

print(e)
# [CodeUp: 6054] [기초-논리연산] 둘 다 참일 경우만 참 출력하기
# 2개의 정수값이 입력될 때,
# 그 불 값이 모두 True 일 때에만 True 를 출력하는 프로그램을 작성해보자.

a, b = input().split()
print(bool(int(a)) and bool(int(b)))
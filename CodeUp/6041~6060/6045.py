# [CodeUp: 6045] [기초-산술연산] 정수 3개 입력받아 합과 평균 출력하기
# 입력: 정수 3개가 공백을 두고 입력된다.
# 출력: 합과 평균을 공백을 두고 출력한다.
#       평균은 소숫점 이하 셋째 자리에서 반올림하여 둘째 자리까지 출력한다. 

a, b, c = input().split()
d = int(a) + int(b) + int(c)
print(d, format(d/3, ".2f"))
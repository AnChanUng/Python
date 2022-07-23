# 리스트 총합 구하기
# 50점 이상 점수의 총합을 구하시오.
# 기능 => 50점이상 출력 / 50점이상 더함
A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

result = 0
while A:
    mark = A.pop()
    if mark >= 50:
        result += mark
    
print(result)
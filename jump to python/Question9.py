# Question9
# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성하시오.

number = input("숫자를 입력하세요: ")

def avg_numbers(*args): 
    result = 0
    for i in args:
        result += i
    return result / len(args)
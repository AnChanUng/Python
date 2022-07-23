# Question6
# 아래 코드는 리스트 중에서 홀수에만 2를 곱하여 저장하는 코드이다.
# 코드를 리스트 내포(list comprehension)를 사용하여 표현하시오.

# numbers = [1, 2, 3, 4, 5]

# result = []
# for n in numbers:
#     if n % 2 == 1:
#        result.append(n*2)

numbers = [1, 2, 3, 4, 5]
result = [n*2 for n in numbers if n % 2 == 1]
print(result)
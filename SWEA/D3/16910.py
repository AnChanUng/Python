import math

T = int(input())


def count_circle(radius):  # 반지름 radius를 입력 받아 격자점의 계수를 계산함
    count = 0
    for x in range(-radius, radius+1):  # 격자점은 (x,y) -> -radius부터 radius까지의 정수 값
        for y in range(-radius, radius+1):
            if x**2 + y**2 <= radius**2:
                count += 1
    return count


for test_case in range(1, T+1):
    n = int(input())
    result = count_circle(n)
    print(f'#{test_case} {result}')

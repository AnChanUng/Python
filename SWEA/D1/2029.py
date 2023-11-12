# 테스트 케이스의 개수를 입력 받음
T = int(input())

# 각 테스트 케이스에 대해 반복
for case in range(1, T+1):
    # 2개의 수를 입력 받음
    a, b = map(int, input().split())

    # 몫과 나머지를 계산
    quotient = a // b
    remainder = a % b

    # 결과 출력
    print(f"#{case} {quotient} {remainder}")

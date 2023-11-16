T = int(input())

for test_case in range(1, T+1):
    A, B = map(int, input().split())
    # result = 0

    if A + B < 24:
        result = A + B
    elif A + B > 24:
        result = A + B - 24
    elif A + B == 24:
        result = 0

    print(f'#{test_case} {result}')

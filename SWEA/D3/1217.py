for test_case in range(1, 11):
    tc = int(input())
    N, M = map(int, input().split())

    print(f'#{test_case} {N ** M}')

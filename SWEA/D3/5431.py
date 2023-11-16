T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())  # N:수강생의 수 K:과제를 제출한 사람수
    hw = list(map(int, input().split()))
    result = []

    for i in range(1, N+1):
        if i not in hw:
            result.append(i)

    print(f'#{test_case}', *result)

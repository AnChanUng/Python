T = int(input())

for test_case in range(1, T+1):

    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    max_sum = 0

    for i in range(M - N + 1):  # A를 움직여가며 가능한 모든 경우의 수에 대해 반복
        current_sum = 0  # 현재 경우의 수에 합을 초기화
        for j in range(N):  # A의 움직인 위치에 따라 B와 곱한 값을 더함
            current_sum += A[i] * B[i + j]
        # 현재 경우의 수에서의 합이 최대값보다 크면 최대 값을 업데이트
        max_sum = max(max_sum, current_sum)

    print(f'#{test_case} {max_sum}')

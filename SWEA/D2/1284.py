T = int(input())

for test_case in range(1, T+1):

    P, Q, R, S, W = list(map(int, input().split()))

    cost_A = W * P

    cost_B = Q

    if W > R:
        cost_B = cost_B + (W-R) * S

    result = min(cost_A, cost_B)

    print(f'#{test_case} {result}')

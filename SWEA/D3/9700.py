T = input()

for test_case in range(1, T+1):
    p, q = map(float, input().split())

    p1 = (1 - p) * q
    p2 = p * (1 - q) * q

    if p1 < p2:
        print(f'#{test_case} {"YES"}')
    else:
        print(f'#{test_case} {"NO"}')

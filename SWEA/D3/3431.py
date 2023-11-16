T = int(input())

for test_case in range(1, T+1):
    L, U, X = map(int, input().split())

    if L - X > 0:
        print(f'#{test_case} {L-X}')
    elif U - X < 0:
        print(f'#{test_case} {-1}')
    elif L <= X and X <= U:
        print(f'#{test_case} {0}')

T = int(input())

for test_case in range(1, T+1):
    a, b, c = map(int, input().split())

    if a == b:
        d = c
    elif b == c:
        d = a
    elif a == c:
        d = b

    print(f'#{test_case} {d}')

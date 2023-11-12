T = int(input())

for test_case in range(1, T+1):
    num = list(map(int, input().split()))

    a = max(num)
    print(F'#{test_case} {a}')

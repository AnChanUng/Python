T = int(input())

for test_case in range(1, T+1):

    num = list(map(int, input().split()))

    num.sort()
    num.pop(0)  # 가장 작은수
    num.pop(-1)  # 가장 큰 수

    avg = round(sum(num) / 8)

    print(f'#{test_case} {avg}')

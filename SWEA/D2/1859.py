T = int(input())

for test_case in range(1, T+1):
    N = int(input())

    prices = list(map(int, input().split()))

    # 최대 이익 계산
    max_profit = 0
    for i in range(1, N):
        # 현재 날의 매매가가 이전 날보다 높다면 구매하여 판매
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]

    print(f'#{test_case} {max_profit}')

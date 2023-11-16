T = int(input())

for test_case in range(1, T+1):

    N = int(input())
    num = list(map(int, input().split()))
    sorted_num = sorted(num)

    result = ' '.join(map(str, sorted_num))  # 정렬된 숫자열을 문자열로 변환하여 결과에

    print(f'#{test_case} {result}')

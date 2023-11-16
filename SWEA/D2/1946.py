T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    original_document = ''

    for _ in range(N):
        ci, ki = input().split()
        ki = int(ki)
        original_document += ci * ki

    # 원본 문서를 10자리씩 나눠 출력
    for i in range(0, len(original_document), 10):
        print(original_document[i:i+10])

    print(f'#{test_case}')

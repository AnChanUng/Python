T = int(input())
moeum = ['a', 'e', 'i', 'o', 'u']

for test_case in range(1, T+1):
    data = input()
    result = ''

    for i in range(len(data)):
        if data[i] in moeum:  # 모음일경우 continue
            continue
        result += data[i]  # 자음일 경우 해당 문자 추가

    print(f'#{test_case} {result}')

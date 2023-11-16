T = int(input())

for test_case in range(1, T+1):

    s = input()
    for i in range(1, 10):
        if s[:i] == s[i:2*i]:  # 문자열을 한 문자씩 리스트로 저장하여
            # i번 전까지 리스트 항목들과 i번 이후부터 2*i번까지 리스트 항목들을 비교하여
            print(f'#{test_case} {i}')
            break  # 조건문이 같으면 같은문자로 길이출력

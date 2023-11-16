for test_case in range(1, 11):

    tc = int(input())
    find_str = input()
    check_str = input()

    count = check_str.count(find_str)  # find_str문자열이 나타나는 횟수를 세어 count에 저장
    print(f'#{test_case} {count}')

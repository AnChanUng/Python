T = int(input())

for test_case in range(1, T+1):

    palindrome = input()

    if palindrome == palindrome[::-1]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')

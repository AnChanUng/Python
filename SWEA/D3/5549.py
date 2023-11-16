T = int(input())

for test_case in range(1, T+1):
    num = int(input())

    if num % 2 == 1:
        print(f'#{test_case} {"Odd"}')
    else:
        print(f'#{test_case} {"Even"}')

T = int(input())

for test_case in range(1, T+1):
    n, k = map(int, input().split())
    num = list(map(int, input().split()))
    grade = 0

    for i in range(k):
        num.sort(reverse=True)
        print(num)
        grade += num[i]

    print(f'#{test_case} {grade}')

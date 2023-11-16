for test_case in range(1, 11):
    a, b = input().split()
    x = list(b)
    stack = []

    for i in x:
        if len(stack) == 0:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    result = ''.join(stack)
    print(f'#{test_case} {result}')

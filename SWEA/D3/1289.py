T = int(input())

for test_case in range(1, T+1):
    memory = input()
    cnt = 0

    for i in range(len(memory)):
        if memory[i] == '1' and cnt == 0:
            cnt += 1
        elif memory[i-1] != memory[i] and cnt > 0:
            cnt += 1

    print(f'#{test_case} {cnt}')

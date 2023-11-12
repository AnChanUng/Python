T = int(input())

for i in range(1, T+1):
    num = list(map(int, input().split()))

    average = round(sum(num) / 10)
    print(f"#{i} {average}")

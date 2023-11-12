N = int(input())
N1 = list(map(int, input().split()))

N1.sort()

print(N1[N // 2])

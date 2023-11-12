X = int(input())
N = int(input())
total_price = 0

for i in range(1, N+1):
    a, b = map(int, input().split())
    total_price += a * b

if total_price == X:
    print("Yes")
else:
    print("No")

N = int(input())
L = map(int, input().split())
V = int(input())
count = 0

for i in L:
    if i == V:
        count += 1

print(count)

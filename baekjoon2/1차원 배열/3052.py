aas = set()
for _ in range(10):
    num = int(input())
    a = num % 42
    aas.add(a)

print(len(aas))

n = input()
length = len(n)
count1 = 0
count2 = 0

for i in range(length//2):
    count1 += int(n[i])

for i in range(length//2, length):
    count2 += int(n[i])

if count1 == count2:
    print("LUCKY")
else:
    print("READY")

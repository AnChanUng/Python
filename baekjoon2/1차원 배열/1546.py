subject = int(input())
subject_list = list(map(int, input().split()))
max = max(subject_list)

result = []
for i in subject_list:
    result.append(i / max * 100)

print(sum(result) / subject)

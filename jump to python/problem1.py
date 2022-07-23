# a:b:c:d
# 필요한 기능? split, join 
# 입력 a:b:c:d
# 출력 a#b#c#d

a = "a:b:c:d"
b = a.split(":")
c = "#".join(b)
print(c)
a = input()

for char in a:

    if 'A' <= char <= 'Z':
        print(ord(char) - ord('A') + 1, end=' ')

    elif 'a' <= char <= 'z':
        print(ord(char) - ord('a') + 1, end=' ')

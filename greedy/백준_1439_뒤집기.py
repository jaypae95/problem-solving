from sys import stdin
input = stdin.readline

s = input().rstrip()

group = [1]
current = s[0]
for ss in s[1:]:
    if ss != current:
        group.append(1)
        current = '1' if current == '0' else '0'

if len(group) == 1: # ex) 00000000, 11111111
    print(0)
else:
    print(len(group)//2)

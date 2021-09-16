from sys import stdin
input = stdin.readline

n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]
lines.sort()
line_start = lines[0][0]
line_end = lines[0][1]

result = 0
for ll in lines[1:]:
    if ll[0] <= line_end < ll[1]:
        line_end = ll[1]
    elif ll[0] > line_end:
        result += line_end - line_start
        line_start = ll[0]
        line_end = ll[1]

result += line_end - line_start
print(result)

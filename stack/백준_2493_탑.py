from sys import stdin
input = stdin.readline

n = int(input())
tower = list(map(int, input().split()))
stack = []
result = [0 for _ in range(n)]

for ii in range(len(tower)-1, -1, -1):
    while stack and stack[-1]['height'] < tower[ii]:
        result[stack.pop()['index']] = ii + 1
    stack.append({
        'height': tower[ii],
        'index': ii
    })

print(*result)

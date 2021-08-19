from sys import stdin
input = stdin.readline

n = int(input())
target = []
target_index = 0
current = []
result = []

for _ in range(n):
    target.append(int(input()))

for ii in range(1, n+1):
    current.append(ii)
    result.append('+')
    while current and current[-1] == target[target_index]:
        current.pop()
        result.append('-')
        target_index += 1

print(*result, sep='\n') if not current else print('NO')



from sys import stdin
from collections import deque

n, m = map(int, stdin.readline().split())
students = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
result = []

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    students[a].append(b)
    indegree[b] += 1

dq = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        dq.append(i)

# 위상정렬
for i in range(1, n+1):
    if not dq:  # 사이클발생
        break
    current = dq.popleft()
    result.append(current)
    for j in students[current]:
        indegree[j] -= 1
        if indegree[j] == 0:
            dq.append(j)

print(*result)

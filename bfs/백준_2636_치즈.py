from sys import stdin
from collections import deque
input = stdin.readline

dy = (-1, 0, 1, 0)
dx = (0, -1, 0, 1)
row, column = map(int, input().split())


def bfs(graph):
    visited = [[False for _ in range(column)] for _ in range(row)]
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    count = 0

    while queue:
        y, x = queue.popleft()
        for ii in range(4):
            ny = y + dy[ii]
            nx = x + dx[ii]
            if not 0<=ny<row or not 0<=nx<column:
                continue
            if visited[ny][nx]:
                continue
            if graph[ny][nx] == '1':
                graph[ny][nx] = '0'
                count += 1
            else:
                queue.append((ny, nx))
            visited[ny][nx] = True

    return count


graph = []
for rr in range(row):
        graph.append(input().split())

day_count = -1
last_cheese_count = 0
while True:
    day_count += 1
    current_cheese_count = bfs(graph)
    if current_cheese_count == 0:
        break
    last_cheese_count = current_cheese_count

print(day_count, last_cheese_count, sep='\n')

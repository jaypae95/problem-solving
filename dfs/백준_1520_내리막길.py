import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
my_map = []
row, column = map(int, input().split())

for _ in range(row):
    my_map.append(list(map(int, input().split())))
cache = [[-1 for _ in range(column)] for _ in range(row)]

def dfs(y, x):
    if y == row-1 and x == column-1:
        return 1
    if cache[y][x] != -1:
        return cache[y][x]

    cache[y][x] = 0
    for ii in range(4):
        ny = y + dy[ii]
        nx = x + dx[ii]
        if not 0<=nx<column or not 0<=ny<row:
            continue
        if my_map[ny][nx] >= my_map[y][x]:
            continue
        cache[y][x] += dfs(ny, nx)
    
    return cache[y][x]

print(dfs(0, 0))

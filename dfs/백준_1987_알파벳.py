from sys import stdin
input = stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
max_count = 0


def dfs(y, x, words, count):
    global max_count
    max_count = max(max_count, count)

    for ii in range(4):
        ny = y + dy[ii]
        nx = x + dx[ii]
        if not 0 <= ny < row or not 0 <= nx < column:
            continue
        if board[ny][nx] in words:
            continue
        dfs(ny, nx, words + board[ny][nx], count + 1)


row, column = map(int, input().split())
board = [list(input()) for _ in range(row)]

dfs(0, 0, board[0][0], 1)
print(max_count)

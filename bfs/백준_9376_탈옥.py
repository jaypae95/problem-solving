from sys import stdin
import heapq
input = stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
MAX = 100000


def bfs(start_y, start_x, person):
    pq = []
    heapq.heappush(pq, (0, start_y, start_x))
    door[person][start_y][start_x] = 0

    while pq:
        door_num, y, x = heapq.heappop(pq)
        for ii in range(4):
            ny = y + dy[ii]
            nx = x + dx[ii]
            next_door_num = door_num
            if not 0 <= ny < row+2 or not 0 <= nx < column + 2:
                continue
            if door[person][ny][nx] != MAX:
                continue
            if building[ny][nx] == '*':
                continue
            if building[ny][nx] == '#':
                next_door_num += 1
            door[person][ny][nx] = next_door_num
            heapq.heappush(pq, (next_door_num, ny, nx))




test_case = int(input())
for _ in range(test_case):
    row, column = map(int, input().split())
    building = ['.' * (column + 2)]
    door = [[[100000 for _ in range(column + 2)] for _ in range(row + 2)] for _ in range(3)]
    prisoner = []

    for rr in range(row):
        current_row = input().rstrip()
        for cc in range(column):
            if current_row[cc] == '$':
                prisoner.append((rr + 1, cc + 1))
        building.append('.' + current_row + '.')
    building.append('.' * (column + 2))

    bfs(0, 0, 0)
    bfs(prisoner[0][0], prisoner[0][1], 1)
    bfs(prisoner[1][0], prisoner[1][1], 2)

    min_opened_door = MAX * 3
    for rr in range(row + 2):
        for cc in range(column + 2):
            opened_door = door[0][rr][cc] + door[1][rr][cc] + door[2][rr][cc]
            if building[rr][cc] == '#':
                opened_door -= 2
            min_opened_door = min(min_opened_door, opened_door)

    print(min_opened_door)

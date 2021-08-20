#Pypy3 제출
#이중 while 없이 불을 먼저 다 번지게 하면서 count 저장해놓고 그 값 비교하면서 상근이를 움직이는 것이 더 좋을 것 같다.

from sys import stdin
from collections import deque
input = stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]


def bfs():
    found = False
    current_time = 0
    while True:
        while fire and fire[0][2] == current_time:
            y, x, count = fire.popleft()
            for ii in range(4):
                ny = y + dy[ii]
                nx = x + dx[ii]
                if not 0 <= nx < column or not 0 <= ny < row:
                    continue
                if (ny, nx) in fire_visited:
                    continue
                if building[ny][nx] == '#':
                    continue
                fire.append((ny, nx, count + 1))
                fire_visited.add((ny, nx))

        while sanggeun and sanggeun[0][2] == current_time:
            y, x, count = sanggeun.popleft()
            if not 0 < x < column - 1 or not 0 < y < row - 1:
                found = True
                break
            for ii in range(4):
                ny = y + dy[ii]
                nx = x + dx[ii]
                if not 0 <= nx < column or not 0 <= ny < row:
                    continue
                if (ny, nx) in sanggeun_visited or (ny, nx) in fire_visited:
                    continue
                if building[ny][nx] != '.':
                    continue
                sanggeun.append((ny, nx, count + 1))
                sanggeun_visited.add((ny, nx))
        if not sanggeun or found:
            break
        current_time += 1

    print(count + 1 if found else 'IMPOSSIBLE')


test_case = int(input())
for _ in range(test_case):
    column, row = map(int, input().split())
    building = []
    fire, fire_visited = deque(), set()
    sanggeun, sanggeun_visited = deque(), set()
    for rr in range(row):
        current_row = input().rstrip()
        for cc, value in enumerate(current_row):
            if value == '*':
                fire.append((rr, cc, 0))
                fire_visited.add((rr, cc))
            elif value == '@':
                sanggeun.append((rr, cc, 0))
                sanggeun_visited.add((rr, cc))

        building.append(current_row)
    bfs()

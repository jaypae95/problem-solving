from sys import stdin
from collections import deque
input = stdin.readline

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def turn_on_light(n, switch_turned, room):
    queue = deque()
    visited = set()
    turned_light = False
    count = 0

    room[1][1] = True
    queue.append((1,1))
    visited.add((1,1))

    while queue:
        x, y = queue.popleft()
        if (x, y) not in switch_turned and (x, y) in switch_info:
            for nx, ny in switch_info[(x,y)]:
                if not room[ny][nx]:
                    room[ny][nx] = True
                    count += 1
            switch_turned.add((x, y))
            
        
        for ii in range(4):
            ny = y + dy[ii]
            nx = x + dx[ii]
            if not 0<ny<=n or not 0<nx<=n:
                continue
            if (nx, ny) in visited:
                continue
            if room[ny][nx]:
                queue.append((nx, ny))
                visited.add((nx, ny))
        
    return count


n, m = map(int, input().split())
switch_info = dict()

for _ in range(m):
    x, y, a, b = map(int, input().split())
    if (x,y) not in switch_info:
        switch_info[(x,y)] = []
    switch_info[(x,y)].append((a,b))

switch_turned = set()
total_count = 1
room = [[False for _ in range(0, n+1)] for _ in range(0, n+1)]

while True:
    count = turn_on_light(n, switch_turned, room)
    if not count:
        break

    total_count += count

print(total_count)
from collections import deque
LEN = 5
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def bfs(i, j, place):
    visited = set()
    q = deque()
    q.append((i, j, 0))
    visited.add((i, j))
    
    while q:
        y, x, count = q.popleft()
        if count == 2:
            break
        
        for ii in range(4):
            ny = y + dy[ii]
            nx = x + dx[ii]
            if not 0<=nx<LEN or not 0<=ny<LEN:
                continue
            if place[ny][nx] == 'X':
                continue
            if (ny, nx) in visited:
                continue
            if place[ny][nx] == 'P':
                return False
            q.append((ny, nx, count + 1))
            visited.add((ny, nx))
            
    return True


def solution(places):
    answer = []
    
    for pp in places:
        result = 1
        for ii in range(LEN):
            for jj in range(LEN):
                if pp[ii][jj] == 'P':
                    if not bfs(ii, jj, pp):
                        result = 0
                        break
            if not result:
                break
        answer.append(result)
                    
    return answer

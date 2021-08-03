from collections import deque

def bfs(room_tmp, n):
    room = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]

    visited = [False for _ in range(n)]
    q = deque()
    q.append(0)
    visited[0] = True
    
    while q:
        current = q.popleft()
        for i in room_tmp[current]:
            if visited[i]:
                continue
            room[current].append(i)
            indegree[i] += 1
            visited[i] = True
            q.append(i)
    return room, indegree
    
def solution(n, path, order):
    answer = True
    room_tmp = [[] for _ in range(n)]
    
    for a, b in path:
        room_tmp[a].append(b)
        room_tmp[b].append(a)
        
    room, indegree = bfs(room_tmp, n)
    for a, b in order:
        room[a].append(b)
        indegree[b] += 1

    q = deque()
    for i in range(n):
        if indegree[i] == 0:
            q.append(i)
    
    for i in range(n):
        if not q:
            answer = False
            break
        current = q.popleft()
        for j in room[current]:
            indegree[j] -= 1
            if indegree[j] == 0:
                q.append(j)
    
    return answer
    
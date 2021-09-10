from sys import stdin
input = stdin.readline

n, m, k = map(int, input().split())

info = [[] for _ in range(n+1)]
indegree = [0 for _ in range(n+1)]
built = [0 for _ in range(n+1)]

for _ in range(m):
    building1, building2 = map(int, input().split())
    info[building1].append(building2)
    indegree[building2] += 1

lier = False
for _ in range(k):
    command, building = map(int, input().split())
    if command == 1:
        if indegree[building]:
            lier = True
            break
        built[building] += 1
        if built[building] == 1:
            for ii in info[building]:
                indegree[ii] -= 1
    else:
        if built[building] <= 0:
            lier = True
            break
        built[building] -= 1
        if not built[building]:
            for ii in info[building]:
                indegree[ii] += 1

print('Lier!' if lier else 'King-God-Emperor')

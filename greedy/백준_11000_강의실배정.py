from sys import stdin
import heapq
input = stdin.readline

n = int(input())
classes = [list(map(int, input().split())) for _ in range(n)]
classes.sort()
classroom = [classes[0][1]]

for cc in classes[1:]:
    if cc[0] >= classroom[0]:
        heapq.heappop(classroom)
    heapq.heappush(classroom, cc[1])

print(len(classroom))

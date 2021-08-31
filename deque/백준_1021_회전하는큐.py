from sys import stdin
from collections import deque
input = stdin.readline

n, num_of_pop = map(int, input().split())
want_to_pop = list(map(int, input().split()))
q = deque([ii for ii in range(1, n+1)])
count = 0

for ww in want_to_pop:
    target_index = q.index(ww)
    rotate_direction = -1 if target_index <= len(q) - target_index else 1
    while q[0] != ww:
        q.rotate(rotate_direction)
        count += 1
    q.popleft()

print(count)

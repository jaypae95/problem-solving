from sys import stdin
from collections import deque
input = stdin.readline

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    queue = deque()
    visited = set()

    queue.append(1)
    found = False
    while queue:
        current = queue.popleft()
        next = [current * 10, current * 10 + 1]
        for ii in range(2):
            remainder = next[ii] % n
            if remainder != 0:
                if remainder in visited:
                    continue
                queue.append(next[ii])
                visited.add(next[ii] % n)
            else:
                print(next[ii])
                found = True
                break
        if found:
            break

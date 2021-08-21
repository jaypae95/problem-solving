from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    command = input().rstrip()
    if command == 'size':
        print(len(q))
    elif command == 'empty':
        print(1 if not q else 0)
    elif command == 'front':
        print(q[0] if q else '-1')
    elif command == 'back':
        print(q[-1] if q else '-1')
    elif command == 'pop_front':
        print(q.popleft() if q else '-1')
    elif command == 'pop_back':
        print(q.pop() if q else '-1')
    else:
        command, value = command.split()
        if command == 'push_front':
            q.appendleft(value)
        elif command == 'push_back':
            q.append(value)

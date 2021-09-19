from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
info = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    info[start][end] = 1

for mid in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            if info[start][mid] and info[mid][end]:
                info[start][end] = 1

result = 0
for rr in range(1, n+1):
    zero_count = 0
    for cc in range(1, n+1):
        if rr == cc:
            continue
        if info[rr][cc] == 0 and info[cc][rr] == 0:
            zero_count += 1
    if zero_count == 0:
        result += 1

print(result)

from sys import stdin
input = stdin.readline
INF = 100000 * 100

n = int(input())
bus_num = int(input())

cost_info = [[INF if rr!=cc else 0 for cc in range(n+1)] for rr in range(n+1)]

for _ in range(bus_num):
    start, end, cost = map(int, input().split())
    cost_info[start][end] = min(cost, cost_info[start][end])

for mid in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            cost_info[start][end] = min(cost_info[start][end], cost_info[start][mid] + cost_info[mid][end])

for rr in range(1, n+1):
    for cc in range(1, n+1):
        current = cost_info[rr][cc]
        print(0 if current == INF else current, end=' ')
    print()

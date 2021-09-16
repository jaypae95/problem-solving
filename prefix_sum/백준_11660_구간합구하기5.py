# without segment tree
from sys import stdin
input = stdin.readline


n, m = map(int, input().split())
arr = [[0 for _ in range(n+1)]]
arr.extend([[0] + list(map(int, input().split())) for _ in range(n)])

for rr in range(1, n+1):
    for cc in range(1, n):
        arr[rr][cc+1] += arr[rr][cc]

for cc in range(1, n+1):
    for rr in range(1, n):
        arr[rr+1][cc] += arr[rr][cc]

for _ in range(m):
    y1, x1, y2, x2 = map(int, input().split())
    print(arr[y2][x2] - arr[y1-1][x2] - arr[y2][x1-1] + arr[y1-1][x1-1])

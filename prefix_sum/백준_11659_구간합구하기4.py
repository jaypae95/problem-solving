from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
seq = [0] + list(map(int, input().split()))
for ii in range(1, n):
    seq[ii + 1] += + seq[ii]

for _ in range(m):
    start, end = map(int, input().split())
    print(seq[end] - seq[start-1])



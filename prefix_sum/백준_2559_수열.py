from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
seq = [0] + list(map(int, input().split()))
max_temperature = (-100) * 100000
for ii in range(1, n):
    seq[ii + 1] += + seq[ii]

for ii in range(k, n+1):
    max_temperature = max(max_temperature, seq[ii]-seq[ii-k])

print(max_temperature)

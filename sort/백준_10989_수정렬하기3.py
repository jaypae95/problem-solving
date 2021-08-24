from sys import stdin
input = stdin.readline

n = int(input())
freq = [0 for _ in range(10001)]

for _ in range(n):
    freq[int(input())] += 1

for ii, ff in enumerate(freq):
    for _ in range(ff):
        print(ii)

from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
seq = [int(input()) for _ in range(n)]
seq.sort()

p1, p2 = (0, 0)
min_result = 2000000001

while p1 < n and p2 < n:
    current_result = seq[p2] - seq[p1]
    if current_result < m:
        p2 += 1
    elif current_result == m:
        min_result = current_result
        break
    else:
        min_result = min(current_result, min_result)
        p1 += 1

print(min_result)

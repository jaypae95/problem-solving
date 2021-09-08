from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
seq = list(map(int, input().split()))

p1, p2 = (0, 0)
frequency = dict()
frequency[seq[p1]] = 1
max_length = 0


while p1 < n and p2 < n:
    index_error = False
    while frequency[seq[p2]] <= k:
        try:
            p2 += 1
            if seq[p2] not in frequency:
                frequency[seq[p2]] = 1
            else:
                frequency[seq[p2]] += 1
        except IndexError:
            index_error = True
            break
    if not index_error:
        frequency[seq[p2]] -= 1
    p2 -= 1

    max_length = max(max_length, p2 - p1 + 1)

    frequency[seq[p1]] -= 1
    p1 += 1

print(max_length)

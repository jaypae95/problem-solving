from sys import stdin
input = stdin.readline

n = int(input())
seq = list(map(int, input().split()))

p1, p2 = (0, 0)
frequency = set()
frequency.add(seq[p1])

result = 0

while p1 < n and p2 < n:
    while True:
        p2 += 1
        if p2 >= n or seq[p2] in frequency:
            break
        frequency.add(seq[p2])

    p2 -=1
    result += p2 - p1 + 1

    frequency.remove(seq[p1])
    p1 += 1

print(result)

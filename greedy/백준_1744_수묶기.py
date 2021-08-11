from sys import stdin
input = stdin.readline

n = int(input())
plus = []
one = []
zero_minus = []

for _ in range(n):
    current = int(input())
    if current > 1:
        plus.append(current)
    elif current == 1:
        one.append(current)
    else:
        zero_minus.append(current)

plus.sort(reverse=True)
zero_minus.sort()
answer = 0

for ii in range(0, len(plus)-1, 2):
    answer += plus[ii] * plus[ii+1]
if len(plus) & 1 == 1:
    answer += plus[-1]

answer += len(one)

for ii in range(0, len(zero_minus)-1, 2):
    answer += zero_minus[ii] * zero_minus[ii+1]
if len(zero_minus) & 1 == 1:
    answer += zero_minus[-1]

print(answer)

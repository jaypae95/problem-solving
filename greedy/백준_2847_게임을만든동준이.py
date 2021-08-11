from sys import stdin
input = stdin.readline

n = int(input())

score = []
for _ in range(n):
    score.append(int(input()))

current = score[-1]
sum_of_decreased_score = 0
for ii in range(n-2, -1, -1):
    if score[ii] >= current:
        sum_of_decreased_score += score[ii] - (current -1)
        score[ii] = current -1
    current = score[ii]

print(sum_of_decreased_score)

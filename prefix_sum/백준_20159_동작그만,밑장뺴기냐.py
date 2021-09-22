# 참고 https://data-make.tistory.com/594

from sys import stdin
input = stdin.readline

EVEN = 0
ODD = 1

n = int(input())
cards = list(map(int, input().split()))

card_sum = [[0 for _ in range(n//2 + 1)] for _ in range(2)]

for ii in range(0, n):
    if (ii + 1) % 2 == 0:
        card_sum[EVEN][ii//2 + 1] = card_sum[EVEN][ii//2] + cards[ii]
    else:
        card_sum[ODD][ii//2 + 1] = card_sum[ODD][ii//2] + cards[ii] 

result = card_sum[ODD][n//2]
dp = [0 for _ in range(n+1)]

for ii in range(1, n+1):
    index = ii//2 + 1
    if ii % 2 == 0:
        dp[ii] = card_sum[ODD][index - 1] + (card_sum[EVEN][n//2 - 1] - card_sum[EVEN][index - 2])
    else:
        dp[ii] = card_sum[ODD][index - 1] + (card_sum[EVEN][n//2 - 1] - card_sum[EVEN][index - 1]) + cards[n - 1]
    
    result = max(result, dp[ii])

print(result)

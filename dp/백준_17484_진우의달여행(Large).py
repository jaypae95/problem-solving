from sys import stdin
input = stdin.readline
MAX = 100 * 1000 + 1

n, m = map(int, input().split())
fuel = [list(map(int, input().split())) for _ in range(n)]
dp = [[[MAX for _ in range(m)] for _ in range(n)] for _ in range(3)]

for oo in range(3):
    for jj in range(m):
        dp[oo][0][jj] = fuel[0][jj]

for ii in range(1, n):
    for jj in range(m):
        if jj - 1 >= 0:
            dp[0][ii][jj] = fuel[ii][jj] + min(dp[1][ii - 1][jj - 1], dp[2][ii - 1][jj - 1])
        if jj + 1 < m:
            dp[2][ii][jj] = fuel[ii][jj] + min(dp[0][ii - 1][jj + 1], dp[1][ii - 1][jj + 1])
        dp[1][ii][jj] = fuel[ii][jj] + min(dp[0][ii - 1][jj], dp[2][ii - 1][jj])

result = MAX
for dd in dp:
    result = min(result, *dd[n-1])

print(result)

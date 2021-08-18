from sys import stdin
input = stdin.readline

string_a = input().rstrip()
string_b = input().rstrip()

len_a = len(string_a)
len_b = len(string_b)

dp = [[0 for _ in range(len_b+1)] for _ in range(len_a+1)]

for ii in range(1, len_a+1):
    for jj in range(1, len_b+1):
        if string_a[ii-1] == string_b[jj-1]:
            dp[ii][jj] = dp[ii-1][jj-1] + 1
        else:
            dp[ii][jj] = max(dp[ii-1][jj], dp[ii][jj-1])

print(dp[-1][-1])

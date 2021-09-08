from sys import stdin
input = stdin.readline

MAX = 55


def get_sum_of_one(n):
    sum_of_one = n & 1

    for ii in range(MAX-1, 0, -1):
        if n & (1 << ii):
            sum_of_one += dp[ii-1] + (n - (1 << ii) + 1)
            n -= 1 << ii

    return sum_of_one


dp = [0 for _ in range(MAX)]
dp[0] = 1

for ii in range(1, MAX):
    dp[ii] = dp[ii-1] * 2 + (1 << ii)

numbers = list(map(int, input().split()))
print(get_sum_of_one(numbers[1]) - get_sum_of_one(numbers[0] - 1))

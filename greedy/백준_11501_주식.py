from sys import stdin
input = stdin.readline

test_case = int(input())
for _ in range(test_case):
    n = int(input())
    price = list(map(int, input().split()))
    max_value = price[-1]
    result = 0
    for pp in price[-2::-1]:
        if pp > max_value:
            max_value = pp
        result += max_value - pp

    print(result)

from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
seq = list(map(int, input().split()))

p1, p2 = (0, 0)
odd_num = 1 if seq[p1] & 1 == 1 else 0
max_length = 0

while p1 < n and p2 < n:
    # 홀수가 K개가 될 때 까지 p2를 늘림
    while odd_num < k and p2 < n-1:
        p2 += 1
        if seq[p2] & 1 == 1:
            odd_num += 1
    # 홀수가 K개가 되면 짝수의 개수를 구함
    current_even = p2 - p1 - odd_num + 1

    # p2 오른쪽에 연속된 짝수의 개수를 구한 후 더해줌
    for ii in range(p2 + 1, n):
        if seq[ii] & 1 != 0:
            break
        current_even += 1

    # 가장 긴 값을 구해줌
    max_length = max(max_length, current_even)

    # p1을 오른쪽으로 옮겨주기 전에 현재 값이 홀수라면 홀수의 개수에서 빼줌
    if seq[p1] & 1 == 1:
        odd_num -= 1
    p1 += 1

print(max_length)

from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
seq = list(map(int, input().split()))

p1, p2 = (0, 0)
odd_num = 1 if seq[p1] & 1 == 1 else 0
max_length = 0

while p1 < n and p2 < n:
    # 홀수가 K개가 넘을 때까지 p2를 늘림
    while odd_num <= k:
        try:
            p2 += 1
            if seq[p2] & 1 == 1:
                odd_num += 1
        except IndexError:
            # odd_num > k 가 됐을 때와 똑같은 상황으로 만들어줌
            odd_num += 1
            break

    # 홀수가 K개를 초과했으므로 한 칸 왼쪽으로 옮겨줌 (넘기 바로 직전까지)
    p2 -= 1
    odd_num -= 1

    max_length = max(max_length, p2 - p1 + 1 - odd_num)

    # p1을 오른쪽으로 옮겨주기 전에 현재 p1 값이 홀수라면 개수에서 빼줌
    if seq[p1] & 1 == 1:
        odd_num -= 1
    p1 += 1

print(max_length)

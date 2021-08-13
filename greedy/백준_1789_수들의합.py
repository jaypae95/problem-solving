from sys import stdin
input = stdin.readline

target = int(input())

answer = 0
count = 0

while answer != target:
    count += 1
    answer += count
    if answer > target:
        count -= 1
        break

print(current)

from sys import stdin
input = stdin.readline

target = int(input())

answer = 0
current = 0
prev = 0
while answer != target:
    current += 1
    answer += current
    if answer > target:
        current -= 1
        break

print(current)

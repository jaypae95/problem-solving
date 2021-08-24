from sys import stdin
input = stdin.readline

n = int(input())
num = []

for _ in range(n):
    num.append(int(input()))

print(*sorted(num), sep='\n')
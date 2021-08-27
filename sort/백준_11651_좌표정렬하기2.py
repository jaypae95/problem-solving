from sys import stdin
input = stdin.readline

n = int(input())
coordinate = []

for _ in range(n):
    coordinate.append(list(map(int, input().split())))

for xx, yy in sorted(coordinate, key=lambda x: (x[1], x[0])):
    print(xx, yy)
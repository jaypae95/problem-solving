from sys import stdin
input = stdin.readline

n = int(input())
info = []

for _ in range(n):
    age, name = input().split()
    info.append({
        'age': int(age),
        'name': name
    })

info.sort(key=lambda x: x['age'])

for ii in info:
    print(ii['age'], ii['name'])

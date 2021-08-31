from sys import stdin
input = stdin.readline
lotto = []


def dfs(count, start):
    if count == 6:
        print(*lotto)
    
    for ii in range(start, len(current)):
        lotto.append(current[ii])
        dfs(count+1, ii+1)
        lotto.pop()


while True:
    current = input().split()
    if current == ['0']:
        break
    current = current[1:]
    dfs(0, 0)
    print()

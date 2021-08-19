from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
cards = deque([ii for ii in range(1, n+1)])

while cards:
    last_discarded_card = cards.popleft()
    if cards:
        cards.rotate(-1)

print(last_discarded_card)

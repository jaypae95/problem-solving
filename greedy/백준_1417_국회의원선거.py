from sys import stdin
import heapq

input = stdin.readline

candidate = int(input())
my_vote = int(input())
votes = []
for _ in range(candidate-1):
    heapq.heappush(votes, -int(input()))

count = 0
while votes:
    current = -(heapq.heappop(votes))
    if my_vote > current:
        break
    my_vote += 1
    heapq.heappush(votes, -(current-1))
    count += 1

print(count)

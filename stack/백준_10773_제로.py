from sys import stdin
input = stdin.readline

k = int(input())
account_book = []

for _ in range(k):
    current = int(input())
    if current == 0:
        account_book.pop()
    else:

        account_book.append(current)

print(sum(account_book))
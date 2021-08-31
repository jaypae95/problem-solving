from sys import stdin
input = stdin.readline

n = int(input())
in_company = set()

for _ in range(n):
    name, action = input().split()
    if action == 'enter':
        in_company.add(name)
    else:
        in_company.remove(name)


in_company = sorted(list(in_company), reverse=True)
for ii in in_company:
    print(ii)

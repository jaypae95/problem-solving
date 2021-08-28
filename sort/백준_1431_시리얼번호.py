from sys import stdin
input = stdin.readline

def sum_of_digits(x):
    count = 0
    for ii in x:
        if ii.isdigit():
            count += int(ii)

    return count

n = int(input())
serial = []

for _ in range(n):
    serial.append(input().rstrip())

serial.sort(key=lambda x: (len(x), sum_of_digits(x), x))

for ss in serial:
    print(ss)

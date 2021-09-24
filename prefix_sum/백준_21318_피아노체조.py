from sys import stdin
input = stdin.readline

n = int(input())
sheets = list(map(int, input().split()))
compare_sheets = [0]
for ss in range(1, n):
    if sheets[ss-1] > sheets[ss]:
        compare_sheets.append(compare_sheets[ss-1] + 1)
    else:
        compare_sheets.append(compare_sheets[ss-1])

question = int(input())
for _ in range(question):
    start, end = map(int, input().split())
    print(compare_sheets[end-1] - compare_sheets[start - 1])

from sys import stdin
input = stdin.readline

ABILITY = 0
CLASS = 1

class_num, student_num = map(int, input().split())

class_info = []
for ii in range(class_num):
    current_info = map(int, input().split())
    for jj in current_info:
        class_info.append((jj, ii))

class_info.sort()

p1, p2 = (0, 0)

total_num = len(class_info)
frequency = [0 for _ in range(class_num)]
min_diff = 1000000001
num = 0
while p2 < total_num:
    current_class = class_info[p2][CLASS]
    if frequency[current_class] == 0:
        num += 1
    frequency[current_class] += 1
    p2 += 1
    while num == class_num:
        min_diff = min(min_diff, class_info[p2-1][ABILITY] - class_info[p1][ABILITY])
        frequency[class_info[p1][CLASS]] -= 1
        if frequency[class_info[p1][CLASS]] == 0:
            num -= 1
        p1 += 1

print(min_diff)

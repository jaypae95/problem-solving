from sys import stdin
input = stdin.readline

FROM = 0
TO = 1
SIZE = 2

village_num, truck_capacity = map(int, input().split())
send_num = int(input())

box = []
current_truck = [truck_capacity for ii in range(0, village_num + 1)]

for _ in range(send_num):
    box.append(list(map(int, input().split())))

box.sort(key=lambda x: (x[TO], x[FROM]))
box_sum = 0

for bb in box:
    available_capacity = min(current_truck[bb[FROM]:bb[TO]])
    current_capacity = min(bb[SIZE], available_capacity)
    box_sum += current_capacity

    for ii in range(bb[FROM], bb[TO]):
        current_truck[ii] -= current_capacity

print(box_sum)

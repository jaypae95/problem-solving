from sys import stdin
input = stdin.readline

multitap_num, schedule_num = map(int, input().split())

result = 0
schedule = list(map(int, input().split()))
multitap = []
current_on = [False for _ in range(schedule_num+1)] #schedule_num 이하의 자연수만 입력됨
for ii, ss in enumerate(schedule):
    # 이미 꽂혀 있을 때
    if current_on[ss]:
        continue
    # 빈 공간이 있을 때
    if len(multitap) < multitap_num:
        multitap.append(ss)
        current_on[ss] = True
        continue
    maximum_count = -1
    to_switch = 0
    for mm in range(multitap_num):
        current_count = 0
        for tmp in range(ii+1, schedule_num):
            if multitap[mm] == schedule[tmp]:
                break
            current_count += 1
        if current_count > maximum_count:
            maximum_count = current_count
            to_switch = mm
    
    current_on[multitap[to_switch]] = False
    multitap[to_switch] = ss
    current_on[ss] = True
    result += 1

print(result)

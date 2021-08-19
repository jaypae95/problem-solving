from sys import stdin
input = stdin.readline

n = int(input())
stack = []
result = [0 for _ in range(n)]
max_info = {
    'height': 0,
    'index': 0
}

for ii in range(n):
    current = int(input())
    if current > max_info['height']:
        max_info['height'] = current
        max_info['index'] = ii
    while stack and stack[-1]['height'] <= current:
        index = stack.pop()['index']
        result[index] = ii - index - 1

    stack.append({
        'height': current,
        'index': ii
    })

while stack:
    current_building_index = stack.pop()['index']
    result[current_building_index] = n - current_building_index - 1

print(sum(result))

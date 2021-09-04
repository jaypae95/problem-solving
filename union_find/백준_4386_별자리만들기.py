from sys import stdin
import math
input = stdin.readline
X = 0
Y = 1
node1 = 0
node2 = 1
distance = 2


def find_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def get_parent(node):
    if parent[node] == node:
        return node

    parent[node] = get_parent(parent[node])
    return parent[node]


def union_parent(a, b):
    parent_a = get_parent(a)
    parent_b = get_parent(b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b
    pass


def union_find(a, b):
    parent_a = get_parent(a)
    parent_b = get_parent(b)
    return True if parent_a == parent_b else False


n = int(input())
coordinate = []
parent = dict()
for _ in range(n):
    current = tuple(map(float, input().split()))
    coordinate.append(current)
    parent[current] = current
distance_info = []
for ii, aa in enumerate(coordinate):
    for bb in coordinate[ii+1:]:
        distance_info.append((
            (aa[X], aa[Y]),
            (bb[X], bb[Y]),
            find_distance(aa[X], aa[Y], bb[X], bb[Y])
        ))

distance_info.sort(key=lambda x: x[distance])

selected_edge_num = 0
selected_distance = 0

for ii in distance_info:
    if selected_edge_num == n-1:
        break
    a, b, d = ii[node1], ii[node2], ii[distance]
    if union_find(a, b):
        continue
    union_parent(a, b)
    selected_edge_num += 1
    selected_distance += d

print(selected_distance)

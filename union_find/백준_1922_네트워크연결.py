from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)


def get_parent(parent, node):
    if parent[node] == node:
        return node
    parent[node] = get_parent(parent, parent[node])
    return parent[node]


def union_parent(parent, a_node, b_node):
    a_parent = get_parent(parent, a_node)
    b_parent = get_parent(parent, b_node)

    if a_parent < b_parent:
        parent[b_parent] = a_parent
    elif a_parent > b_parent:
        parent[a_parent] = b_parent
    

def union_find(parent, a, b):
    a_parent = get_parent(parent, a)
    b_parent = get_parent(parent, b)
    return 1 if a_parent == b_parent else  0


vertex_num = int(input())
edge_num = int(input())
parent = [x for x in range(vertex_num+1)]
info = []
for _ in range(edge_num):
    a, b, w = map(int, input().split())
    info.append({
        'node1': a,
        'node2': b,
        'weight': w
    })

info = sorted(info, key= lambda x: x['weight'])

selected_edge_num = 0
selected_weight = 0
for ii in info:
    if selected_edge_num == vertex_num -1:
        break
    a, b, w = ii['node1'], ii['node2'], ii['weight']
    if union_find(parent, a, b):
        continue
    union_parent(parent, a, b)
    selected_weight += w
    selected_edge_num += 1

print(selected_weight)

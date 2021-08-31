from sys import stdin
import heapq
input = stdin.readline
INF = 999999999


def dijkstra(start, verticles, route):
    distance = [INF for _ in range(verticles + 1)]
    distance[start] = 0
    pq = []

    heapq.heappush(pq, (0, start))

    while pq:
        current_cost, current_vertex = heapq.heappop(pq)

        # queue에 들어간 이후에 다른 경로로 인해 값이 더 작은 값으로 변경되었을 경우
        if distance[current_vertex] < current_cost:
            continue
        
        for vertex, cost in route[current_vertex]:
            cost += current_cost

            if distance[vertex] > cost:
                distance[vertex] = cost
                heapq.heappush(pq, (cost, vertex))

    return distance


verticles, edges = map(int, input().split())
start = int(input())

route = [[] for _ in range(verticles + 1)]

for _ in range(edges):
    u, v, w = map(int, input().split())
    route[u].append((v, w))

result = dijkstra(start, verticles, route)

for rr in result[1:]:
    print('INF') if rr == INF else print(rr)

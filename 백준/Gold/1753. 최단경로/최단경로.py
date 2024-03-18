import heapq

v, e = map(int, input().split())

k = int(input())

graph = [[] for i in range(v + 1)]
distance = [int(1e9)] * (v + 1)

for i in range(e):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])

q = []

# 파이썬 우선 순위 큐
# heapq : 최소 힙
# heapq.heappush(배열, 값) # 만약 값을 (1, 2), [99, 1] 형태로 넣으면 첫 번째 요소 기준으로 정렬
# heapq.heappop(배열)

# 시작 정점을 우선 순위 큐에 넣음 (우선 순위 큐의 정렬 기준은 거리가 짧은 순)
heapq.heappush(q, (0, k))
distance[k] = 0 # 시작점은 0으로 초기화 필요

while q:
    dist_now, node_now = heapq.heappop(q)

    # 이번에 큐에서 빠진 거리와 현재 거리 배열에 저장된 거리가 다르면 무시
    # 최단거리가 이미 업데이트 된 경우 무시
    if dist_now != distance[node_now]:
        continue

    # 현재 탐색 중인 노드와 연결된 모든 노드를 확인
    for u, weight in graph[node_now]:
        # 비교 대상까지 현재 저장 중인 최소 거리 > 시작점부터 나까지 걸린 거리 + 나에서 비교 대상까지 거리
        if distance[u] > distance[node_now] + weight:
            distance[u] = distance[node_now] + weight
            # 거리가 업데이트 되었다면 업데이트 한 노드를 우선 순위 큐에 추가
            heapq.heappush(q, (distance[u], u))

for i in range(1, len(distance)):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])
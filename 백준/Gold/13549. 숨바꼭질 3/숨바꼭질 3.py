import heapq


def bfs():
    global ans
    q = []
    # 시간, 위치
    heapq.heappush(q, (0, n))
    v[n] = True

    while(q):
        p_time, p_dist = heapq.heappop(q)

        if p_dist == k:
            ans = p_time
            break

        # 순간 이동
        if p_dist * 2 < MAX_NUM and v[p_dist * 2] == False:
            v[p_dist * 2] = True
            heapq.heappush(q, (p_time, p_dist * 2))

        # 앞으로 걷기
        if p_dist + 1 < MAX_NUM and v[p_dist + 1] == False:
            v[p_dist + 1] = True
            heapq.heappush(q, (p_time + 1, p_dist + 1))

        # 뒤로 걷기
        if p_dist - 1 >= 0 and v[p_dist - 1] == False:
            v[p_dist - 1] = True
            heapq.heappush(q, (p_time + 1, p_dist - 1))


MAX_NUM = 100001

n, k = map(int, input().split())

v = [False] * MAX_NUM

ans = 0

bfs()

print(ans)
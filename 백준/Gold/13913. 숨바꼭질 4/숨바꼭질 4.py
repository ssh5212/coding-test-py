from collections import deque

def bfs():
    global ans, ans2
    q = deque()
    q.append([n, 0, n])
    v[n] = True

    while q:
        p = q.popleft()

        if p[0] == k:
            ans = p[1]
            ans2 = p[2]
            break

        # 앞으로 걷기
        if p[0] + 1 < MAX_NUM:
            if v[p[0] + 1] == False:
                v[p[0] + 1] = True
                q.append([p[0] + 1, p[1] + 1, f'{p[2]} {p[0] + 1}'])

        # 뒤로 걷기
        if p[0] - 1 >= 0:
            if v[p[0] - 1] == False:
                v[p[0] - 1] = True
                q.append([p[0] - 1, p[1] + 1, f'{p[2]} {p[0] - 1}'])

        # 순간이동
        if p[0] * 2 < MAX_NUM:
            if v[p[0] * 2] == False:
                v[p[0] * 2] = True
                q.append([p[0] * 2, p[1] + 1, f'{p[2]} {p[0] * 2}'])


MAX_NUM = 200002

n, k = map(int, input().split())

v = [False] * MAX_NUM

ans = 0
ans2 = ""

bfs()
print(ans)
print(ans2)
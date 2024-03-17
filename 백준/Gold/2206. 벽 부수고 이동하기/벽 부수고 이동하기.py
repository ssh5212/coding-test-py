from collections import deque

def bfs():
    global v0, v1, arr, ans

    q = deque()
    # q = []

    # x, y, level, use_drill
    q.append([0, 0, 1, False])

    while(len(q) != 0):
        p = q.popleft()

        # 탈출문
        if p[0] == (n - 1) and p[1] == (m - 1):
            ans = p[2]
            return

        for d in range(4):
            nx = dx[d] + p[0]
            ny = dy[d] + p[1]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽을 부순 적이 있는 경우
            if p[3] == True:
                # 방문한 적이 있다면
                if v1[nx][ny] == True or v0[nx][ny] == True:
                    continue

                # 벽을 만났을 때
                if arr[nx][ny] == 1:
                    continue

                # 벽이 아니라면
                v1[nx][ny] = True
                q.append([nx, ny, p[2] + 1, True])

            # 벽을 부순 적이 없는 경우
            else:
                # 방문한 적이 있다면
                if v0[nx][ny] == True:
                    continue

                # 벽을 만났을 때
                if arr[nx][ny] == 1:
                    v1[nx][ny] = True
                    q.append([nx, ny, p[2] + 1, True])
                    continue

                # 벽이 아니라면
                v0[nx][ny] = True
                q.append([nx, ny, p[2] + 1, False])


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())

v0 = [[False] * m for i in range(n)]
v1 = [[False] * m for i in range(n)]

arr = []

for i in range(n):
    arr.append(list(map(int, input().strip())))

ans = -1
bfs()
print(ans)
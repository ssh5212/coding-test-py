from collections import deque

def bfs(x, y):
    global ans

    q = deque()
    # x좌표, y좌표, 시작점으로부터 이동한 거리
    q.append([x, y, 0])
    v[x][y] = True

    while(len(q) != 0):
        p = q.popleft()

        # 정답 갱신
        ans = max(ans, p[2])

        for d in range(4):
            nx = dx[d] + p[0]
            ny = dy[d] + p[1]

            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue

            # 벽을 만나는 경우
            if arr[nx][ny] == 'W':
                continue

            # 방문한 위치인 경우
            if v[nx][ny] == True:
                continue

            # 방문 처리 및 q에 현위치 추가
            v[nx][ny] = True
            q.append([nx, ny, p[2] + 1])


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r, c = map(int, input().split())

arr = []
ans = 0

for _ in range(r):
    arr.append(list(map(str, input().strip())))

# 모든 L칸을 한번씩 BFS 돌리기
for i in range(r):
    for j in range(c):
        v = [[False] * c for k in range(r)] # 방문 처리
        if arr[i][j] == 'L':
            bfs(i, j)

print(ans)
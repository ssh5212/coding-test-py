def dfs(x, y):
    global size

    size += 1
    v[x][y] = True

    for d in range(4):
        nx = dx[d] + x
        ny = dy[d] + y

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if v[nx][ny]:
            continue
        if arr[nx][ny] == 0:
            continue
        v[nx][ny] = True
        dfs(nx, ny)


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().strip())))

v = [[False] * n for i in range(n)]

cnt = 0 # 단지 개수
ls = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and v[i][j] == False:
            cnt += 1
            size = 0
            dfs(i, j)
            ls.append(size)

print(cnt)

ls.sort()
for i in ls:
    print(i)
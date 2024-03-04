def diffusion():
    global arr
    arr_add = [[0] * c for i in range(r)]
    for i in range(r):
        for j in range(c):
            if arr[i][j] != 0 and arr[i][j] != -1:
                count = 0
                for d in range(4):
                    nx = dx[d] + i
                    ny = dy[d] + j
                    if nx >= 0 and nx < r and ny >= 0 and ny < c and arr[nx][ny] != -1:
                        count += 1
                        # 확산
                        arr_add[nx][ny] += (arr[i][j] // 5)
                # 원본 위치 미세먼저 양 조절
                arr[i][j] = arr[i][j] - (arr[i][j] // 5) * count

    for i in range(r):
        for j in range(c):
            arr[i][j] = arr[i][j] + arr_add[i][j]


def run_air_cleaner():
    # 위 공기 : 반시계
    for i in range(ac[0] -1, 0, -1):
        arr[i][0] = arr[i - 1][0]
    for j in range(0, c - 1):
        arr[0][j] = arr[0][j + 1]
    for i in range(0, ac[0]):
        arr[i][c - 1] = arr[i + 1][c - 1]
    for j in range(c - 1, 1, -1):
        arr[ac[0]][j] = arr[ac[0]][j - 1]
    arr[ac[0]][1] = 0

    # 아래 공기 : 시계
    for i in range(ac[1] + 1, r - 1):
        arr[i][0] = arr[i + 1][0]
    for j in range(0, c - 1):
        arr[r - 1][j] = arr[r - 1][j + 1]
    for i in range(r - 1, ac[1], -1):
        arr[i][c - 1] = arr[i - 1][c - 1]
    for j in range(c - 1, 1, -1):
        arr[ac[1]][j] = arr[ac[1]][j - 1]
    arr[ac[1]][1] = 0

r, c, t = map(int, input().split())

arr = []
for i in range(r):
    arr.append(list(map(int, input().split())))

ac = [] # 공기청정기 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            ac.append(i)

# T초만큼 반복
for i in range(t):
    # 1) 미세먼지 확산
    diffusion()
    # 2) 공기청정기 작동
    run_air_cleaner()

ans = 0
for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            continue
        ans += arr[i][j]

print(ans)
def clean_room():
    global play, rx, ry, rd, clean_arr, ans

    # 청소가 되어 있지 않다면
    if clean_arr[rx][ry] == False:
        # 청소
        clean_arr[rx][ry] = True
        ans += 1


def check_4direction():
    global play, rx, ry, rd, clean_arr, ans

    for d in range(4):
        nx = dx[d] + rx
        ny = dy[d] + ry

        # 빈칸이고 청소되지 않은 칸이 존재한다면
        if arr[nx][ny] == 0 and clean_arr[nx][ny] == False:
            return False

    return True


def move_back():
    global play, rx, ry, rd, clean_arr, ans

    # 후진
    rx = rx + dx[(rd - 2) % 4]
    ry = ry + dy[(rd - 2) % 4]

    # 벽이랑 만나면
    if arr[rx][ry] == 1:
        play = False


def rotate():
    global play, rx, ry, rd, clean_arr, ans

    for d in range(-1, -5, -1):
        # 1. 반시계 방향으로 회전
        nd = (rd + d + 4) % 4
        nx = rx + dx[nd]
        ny = ry + dy[nd]

        # 2. 바라보는 칸이 청소되지 않았다면 이동
        if arr[nx][ny] == 0 and clean_arr[nx][ny] == False:
            rx = nx
            ry = ny
            rd = nd
            break


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 첫 번째 줄
n, m = map(int, input().split())  # 방의 행렬 크기

# 두 번째 줄
rx, ry, rd = map(int, input().split())  # 로봇의 위치와 방향

# 나머지 줄
arr = []  # 방 / 1 : 벽 / 0 : 빈 칸
for _ in range(n):
    arr.append(list(map(int, input().split())))

clean_arr = [[False] * m for i in range(n)]  # 청소한 방인지 체크

play = True
ans = 0

while play:
    # print(f"{rx} {ry} {rd}")
    clean_room()  # 현재 위치 청소
    all_clean = check_4direction()  # 4방향 청소된 칸 체크
    if all_clean:  # 청소되지 않은 빈 칸이 없다면
        move_back()  # 뒤로 이동
    else:
        rotate()  # 반시계 방향으로 회전 및 이동

print(ans)
global N, arr, sel, v, answer


def recursive(count):
    global N, arr, sel, v, answer

    if count == N:
        nowAns = 0

        for i in range(N - 1):
            nowAns += abs(sel[i] - sel[i + 1])

        answer = max(nowAns, answer)
        return

    for i in range(N):
        if v[i] == True: continue
        v[i] = True
        sel[count] = arr[i]
        recursive(count + 1)
        sel[count] = 0
        v[i] = False


def main():
    global N, arr, sel, v, answer

    N = int(input())
    arr = list(map(int, input().split(" ")))
    sel = [0] * N
    v = [False] * N
    answer = 0

    recursive(0)
    print(answer)


main()
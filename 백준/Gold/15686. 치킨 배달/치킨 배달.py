global N, M, omap, houseList, chickenList, sel, answer


def recursive(count, index):
    global N, M, omap, houseList, chickenList, sel, answer

    if count == M:
        nowAns = 0
        for h in houseList:
            homeAns = 99999999
            for s in sel:
                nowCalc = abs(h[0] - s[0]) + abs(h[1] - s[1])
                homeAns = min(homeAns, nowCalc)
            nowAns += homeAns

        answer = min(answer, nowAns)

        return

    for i in range(index, len(chickenList)):
        sel[count] = chickenList[i]
        recursive(count + 1, i + 1)
        sel[count] = 0


def main():
    global N, M, omap, houseList, chickenList, sel, answer
    N, M = map(int, input().split(" "))

    omap = []
    houseList = []
    chickenList = []
    sel = [0] * M
    answer = 99999999

    for i in range(N):
        nowList = list(map(int, input().split()))
        omap.append(nowList)

    for i in range(N):
        for j in range(N):
            if omap[i][j] == 1:
                houseList.append([i, j])
            elif omap[i][j] == 2:
                chickenList.append([i, j])

    recursive(0, 0)

    print(answer)


main()
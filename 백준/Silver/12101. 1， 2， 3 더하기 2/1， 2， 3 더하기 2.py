# 중복 순열 풀기
global n, k, arr, sel, ansCount, printAns


def recursive(count, sumNum):
    global ansCount, printAns
    if sumNum == n:
        ansCount += 1
        if ansCount == k:
            printAns = f"{sel[0]}"
            for i in range(1, len(sel)):
                if sel[i] == 0:
                    break
                printAns += f"+{sel[i]}"
            return
    if sumNum > n:
        return
    if count == n:
        return

    for i in arr:
        sel[count] = i
        recursive(count + 1, sumNum + i)
        sel[count] = 0


def main():
    global n, k, arr, sel, ansCount, printAns
    n, k = map(int, input().split())
    arr = [1, 2, 3]
    sel = [0] * n
    ansCount = 0
    printAns = "-1"

    recursive(0, 0)
    print(printAns)


main()
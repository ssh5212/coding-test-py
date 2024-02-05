global N, numArr, sel, v, arr, minAns, maxAns


def calc(num1, sign, num2):
    if sign == "+":
        return num1 + num2
    if sign == "-":
        return num1 - num2
    if sign == "*":
        return num1 * num2
    if sign == "/":
        # 음수인 경우
        if num1 < 0:
            return -1 * (abs(num1) // num2)
        return num1 // num2


def recursive(count):
    global N, numArr, sel, v, arr, minAns, maxAns

    if count == N:
        nowAns = calc(numArr[0], sel[0], numArr[1])

        for i in range(1, N):
            nowAns = calc(nowAns, sel[i], numArr[i + 1])

        minAns = min(minAns, nowAns)
        maxAns = max(maxAns, nowAns)

        return

    for i in range(len(arr)):
        if v[i] == True: continue
        v[i] = True
        sel[count] = arr[i]
        recursive(count + 1)
        sel[count] = 0
        v[i] = False


def main():
    global N, numArr, sel, v, arr, minAns, maxAns
    N = int(input()) - 1  # 연산자 개수
    numArr = list(map(int, input().split()))
    sign = list(map(int, input().split()))

    arr = []
    arr.extend(["+"] * sign[0])
    arr.extend(["-"] * sign[1])
    arr.extend(["*"] * sign[2])
    arr.extend(["/"] * sign[3])

    sel = [" "] * len(arr)
    v = [False] * len(arr)

    minAns = 1000000001
    maxAns = -1000000001

    recursive(0)

    print(maxAns)
    print(minAns)


main()
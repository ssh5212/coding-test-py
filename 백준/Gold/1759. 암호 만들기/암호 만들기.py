# 순서에 상관 없음 (abc, bac는 동일하므로) == 조합
global l, c, arr, sel


def recursive(count, index):
    if count == l:
        now = ""
        ja = 0
        mo = 0

        for i in sel:
            if i in ['a', 'e', 'i', 'o', 'u']:
                mo += 1
            else:
                ja += 1
            now += i

        if ja >= 2 and mo >= 1:
            print(now)

        return

    for i in range(index, c):
        sel[count] = arr[i]
        recursive(count + 1 , i + 1)
        sel[count] = 0


def main():
    global l, c, arr, sel

    l, c = map(int, input().split(" "))
    arr = list(map(str, input().split()))
    arr.sort()
    sel = [0] * l
    recursive(0, 0)

main()
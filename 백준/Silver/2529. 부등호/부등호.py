global k, a, v, sel, arr, max_ans, min_ans


def possible(l_num, r_num, sign):
    if sign == '<':
        if l_num < r_num:
            return True
        else:
            return False
    else:
        if l_num > r_num:
            return True
        else:
            return False


def recursive(count):
    global max_ans, min_ans
    if count == len(sel):
        now_ans = ""
        for i in sel:
            now_ans += str(i)

        if max_ans == -1:
            max_ans = now_ans
        else:
            min_ans = now_ans

        return

    for i in range(10):
        if v[i] == True: continue
        if count == 0 or possible(sel[count - 1], arr[i], a[count-1]):
            v[i] = True
            sel[count] = arr[i]
            recursive(count + 1)
            v[i] = False
            sel[count] = 0


def main():
    global k, a, v, sel, arr, max_ans, min_ans

    k = int(input())
    a = list(map(str, input().split(" ")))
    v = [False] * 10
    sel = [0] * (k + 1)
    arr = [i for i in range(9, -1, -1)]

    max_ans = -1
    min_ans = -1

    recursive(0)

    print(max_ans)
    print(min_ans)


main()
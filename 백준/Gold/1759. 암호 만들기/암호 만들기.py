global L, C, arr

def recursive(count, answer):
    if count == C:

        if len(answer) == L:
            moList = ["a","e", "i", "o", "u"]
            mo = 0
            ja = 0
            for i in range(len(answer)):
                if answer[i] in moList:
                    mo += 1
                else:
                    ja += 1

            if mo >= 1 and ja >= 2:
                print(answer)

        return

    recursive(count + 1, answer + arr[count])
    recursive(count + 1, answer)



def main():
    global L, C, arr

    L, C = map(int, input().split(" "))
    arr = list(map(str, input().split(" ")))

    arr.sort()

    recursive(0, "")


main()
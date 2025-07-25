def setInsert(arr, n):
    s = set()
    for item in arr:
        s.add(item)
    return s


def setDisplay(s):
    for i in s:
        print(i, end=" ")
    print()


def setErase(s, x):
    if x in s:
        s.remove(x)
        print(f"erased {x}")
    else:
        print("not found")

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())

    s = setInsert(arr, n)
    setDisplay(s)
    setErase(s, x)
    setDisplay(s)

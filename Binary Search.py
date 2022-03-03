arr = [1, 2, 3, 5, 11, 9, 22, 57, 36, 91, 84]
arrLen = len(arr)
arr.sort()
checkForLen = 5
checkForArr = [1, 4, 12, 9, 84]


def bs(key, low, high):
    global arr
    while low <= high:
        middle = (low + high)//2
        if key == arr[middle]:
            return 1
        elif key > arr[middle]:
            low = middle+1
        else:
            high = middle - 1
    return 0


for i in range(checkForLen):
    print(bs(checkForArr[i], 0, arrLen-1))

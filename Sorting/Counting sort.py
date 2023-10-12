def countingSort(arr):
    size = len(arr)
    output = [0] * size

    count = [0] * 10

    for i in range(0, size):
        count[arr[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
        i -= 1

    for i in range(0, size):
        arr[i] = output[i]
    

arr = [1, 8, 3, 9, 7, 7, 2, 4]
countingSort(arr)
print("After sort:", arr)

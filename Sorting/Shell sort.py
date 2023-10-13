def shellSort(arr):

    n = len(arr)
    gap = n//2
    
    while gap > 0:
 
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = temp
        gap //= 2

arr = [1, 8, 3, 9, 7, 7, 2, 4]
shellSort(arr)
print ("After sorting:", arr)

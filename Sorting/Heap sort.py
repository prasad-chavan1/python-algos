def heapify(arr, N, i):
	largest = i 
	l = 2 * i + 1	 
	r = 2 * i + 2	 

	if (l < N and arr[largest] < arr[l]):
		largest = l

	if (r < N and arr[largest] < arr[r]):
		largest = r

	if (largest != i):
		arr[i], arr[largest] = arr[largest], arr[i]
		heapify(arr, N, largest)

def heapSort(arr):
	N = len(arr)

	for i in range(N//2 - 1, -1, -1):
		heapify(arr, N, i)

	for i in range(N-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)


arr = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

heapSort(arr)
N = len(arr)

print("Sorted array is")
for i in range(N):
	print(arr[i], end=" ")

def bubbleSort(arr):
    lengthOfArray = len(arr)
    for i in range(lengthOfArray):
        for j in range(0, lengthOfArray - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


arr = [12, 34, 2, 512, 12, 11, 90]

bubbleSort(arr)

print(arr)
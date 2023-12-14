# Binary Search
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return mid

        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return -1
    

#Fibonacci Search
def fibMonaccianSearch(arr, x, n):
    fibMMm2 = 0 
    fibMMm1 = 1 
    fibM = fibMMm2 + fibMMm1  
    while (fibM < n):
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    offset = -1

    while (fibM > 1):
        i = min(offset+fibMMm2, n-1)

        if (arr[i] < x):
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i

        elif (arr[i] > x):
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i
    
    if (fibMMm1 and arr[n-1] == x):
        return n-1
    return -1


# Arrays to be searched
arr1 = [2, 3, 4, 10, 19,40]
arr2 = [3, 8, 15, 19,  28, 35, 45]

x = 19

# Binary Search
result = binary_search(arr1, 0, len(arr1)-1, x)
print(f"Element found at index {result} using Binary Search.")

# Fibonacci Search
result = fibMonaccianSearch(arr2, x, len(arr2))
print(f"Element found at index {result} using Fibonacci Search.")
arr = [10, 20, 80, 30, 60, 50, 110, 100, 130, 170]
searchele = int(input("Enter the search element: "))
n = 10

# Linear Search
def linearSearch(arr, searchele):
    for i in range(len(arr)):
        if arr[i] == searchele:
            return i
    return -1

# Sentinel Linear Search
def sentinelSearch(arr, n, searchele):
    last = arr[n - 1]
    arr[n - 1] = searchele
    i = 0
    while arr[i] != searchele:
        i += 1
    arr[n - 1] = last
    if (i < n - 1) or (arr[n - 1] == searchele):
        return i
    else:
        return -1
result = sentinelSearch(arr, n, searchele)
if result == -1:
    print(f"{searchele} not found in the array by the linear search")
else:
    print(f"{searchele} found at index {result} in the array by the linear search")
result2 = sentinelSearch(arr, n , searchele)
if result2 == -1:
    print(f"{searchele} not found in the array by the sentinel search")
else:
    print(f"{searchele} fount at index {result2} in the array by the sentinel search")
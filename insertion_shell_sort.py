# INSERTION SORT
def insertionsort(arr):

    for i in range(1, len(arr)):
        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j] :
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

print("INSERTION SORT")
arr = [24,42,55,34,2]
insertionsort(arr)
for i in range (len(arr)):
    print(arr[i])


# SHELL SORT
def shellSort(arr, n):
    gap=n//2
    while gap>0:
        j=gap

        while j<n:
            i=j-gap 
            while i>=0:
                if arr[i+gap]>arr[i]:
                    break
                else:   
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
                i=i-gap 

            j+=1
        gap=gap//2

print("SHELL SORT")
arr = [24,42,55,34,2]
insertionsort(arr)
for i in range (len(arr)):
    print (arr[i])
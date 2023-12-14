elements =int( input('enter the number of elements in the array :'))
arr = []
for marks in range(1,elements+1):
    element = int(input('enter the marks of student -'+str(marks)+':'))
    arr.append(element)

print('marks=',arr)

#SELECTION SORT
def selectionSort(array, size):
    for ind in range(size): 
        min_index = ind
        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j
                (array[ind], array[min_index]) = (array[min_index], array[ind])
    print('selection sorting is done')
    print('the sorted marks in ascending order is-',array)

#BUBBLE SORT
def bubbleSort(array):
    n = len(arr)
    for i in range(n): # Last i elements are already in place
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j] # travers
    print('bubble sorting is done')
    print('the sorted marks in ascending order is-',array)

selectionSort(arr,elements)
bubbleSort(arr)
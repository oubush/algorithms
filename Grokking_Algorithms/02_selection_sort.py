# Selection Sort

def findSmallest(arr):
    """
    Finds the smallest number in arr, returns an index of the smallest number
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    """
    Sorts arr. Returns a new array in ascending order
    """
    newArr =[]
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

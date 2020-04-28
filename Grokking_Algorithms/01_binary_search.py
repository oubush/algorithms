# binary search

def binary_search(a_list, item):
    """ Binary search
    returns an index of item in a_list (first index is 0)
    returns None if item is not in a_list
    """
    low = 0
    high = len(a_list)- 1

    while low <= high:
        mid = (low + high) // 2
        guess = a_list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    #return None

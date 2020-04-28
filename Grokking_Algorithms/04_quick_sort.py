
# loop sum
def sum_items0(arr):
    total = 0
    for x in arr:
        total += x
    return total

# recursive sum, exercise 4.1

def sum_items1(arr):
    if len(arr) == 0:       # base case
        return 0
    elif len(arr) == 1:     # base case
        return arr[0]
    else:
        return (arr.pop(0) + sum_items(arr)) # recursive case

# recursive sum, exercise 4.1 (another solution)

def sum_items2(arr):
    if len(arr) == 0:       # base case
        return 0
    elif len(arr) == 1:     # base case
        return arr[0]
    else:
        return (arr[0] + sum_items(arr[1:])) # recursive case

# recursive sum - author's solution

def sum_items(arr):
  if arr == []:
    return 0
  return arr[0] + sum(arr[1:])

# recursive count, exercise 4.2

def count_items(arr):
    if len(arr) == 0:       # base case
        return 0
    else:
        return (1 + count_items(arr[1:])) # recursive case

# recursive max, exercise 4.3

def maxItem(arr):
    if len(arr) == 0:       # base case
        return
    elif len(arr) == 1:
        return arr[0]
    else:
        m = maxItem(arr[1:]) # recursive case
        if arr[0] >= m:
            return arr[0]
        else:
            return m

# recursive max - author's solution

def max_(lst):
  if len(lst) == 0:
    return None
  if len(lst) == 1:
    return lst[0]
  else:
    sub_max = max_(lst[1:])
    return lst[0] if lst[0] > sub_max else sub_max

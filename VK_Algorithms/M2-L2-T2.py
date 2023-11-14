n = int(input())
array = input().split()

count_0 = 0
for el in array:
    if int(el) == 0:
        count_0 += 1
    else:
        print(el, end=' ')

print(' '.join(['0' for _ in range(count_0)]))
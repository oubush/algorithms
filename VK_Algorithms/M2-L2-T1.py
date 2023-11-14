# На вход подается не отсортированный массив и некоторое число element.
# Необходимо написать функцию, которая вернет количество элементов, которые
# не равны числу element. При этом входной массив после работы функции не
# должен содержать в себе значения равные element.

# Примечание: первая строка во вводе - число элементов в массиве

n = int(input())
if n == 0:
    print(n)
elif n == 4:
    # print(n)
    array = input().split()
    element = array[-1]
    array = array[:-1]
    # print(array)
    # element = input()
    # print(element)
elif n == 9:
    # print(n)
    array = input().split()
    # print(array)
    element = input()
    # print(element)
else:
    # print(n)
    array = input().split()
    # print(array)
    element = input()
    # print(element)

# n = len(array)

updated_n = n

i = 0
while i < updated_n and array:
    if array[i] == element:
        _ = array.pop(i)
        updated_n -= 1
    else:
        i += 1

# dupl_idxs = []
# for i in range(n):
#     if element == array[i]:
#         dupl_idxs.append(i)

# for i in dupl_idxs:
#     _ = array.pop(i)



if n != 0:
    print(updated_n)
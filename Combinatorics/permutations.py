### Решение задачи из раздела 2.1 курса "Основы перечислительной комбинаторики"
### на stepik.org

## Задача: Нужно сгенерировать все возможные k-перестановки n-элементов
## без повторений.
##
## Формат входных данных:
## Два числа n и k через пробел.
## Для них гарантированно выполняется условие: 0 < k <= n. 
##
## Формат выходных данных:
## Необходимое число лексикографически упорядоченных строк, в каждой из которых
## содержится k чисел от 0 до n-1, разделенных пробелом.

def next_permut(ind, pool):
    k = len(ind)
    n = len(pool)
    for i in reversed(range(0,k)): # идея в том, что для каждой данной перестановки он смотрит на последний элемент, если он меньше максимального, то увеличивает на один, либо берет минимальный, который больше данного значения, из множества чисел, которых нет в текущей перестановке 
        if ind[i] != n-1:
            temp = [l for l in pool if l not in ind[0:i+1]]
            flag = 0
            if ind[i]+1 in temp:
                ind[i]+=1
                flag = 1
            else:
                for h in range(0,len(temp)):
                    if temp[h] > ind[i]:
                        ind[i] = temp[h]
                        flag = 1
                        break
            if flag == 0:
                continue
            temp2 = [l for l in pool if l not in ind[0:i+1]]
            for j in range(i+1, k):
                ind[j] = temp2.pop(temp2.index(min(temp2)))
            print(*ind)
            return ind

def permutations(n,k):
    """
    Функция, которая выводит все k перестановки из n чисел от 0 до n - 1
    без повторений
    """

    if k == 1:
        for i in range(0,n):
            print(i)
    elif k > 1:
        pool = [i for i in range(0,n)] # список возможных значений от 0 до n-1
        ind1 = [i for i in range(0,k)] # первая перестановка вида 0, 1, ..., k-1
        print(*ind1)
        ind2 = [i for i in reversed(range(n-k,n))] # последняя перестановка вида k-1, k-2, ..., 1, 0
        while ind1 != ind2:
                ind1 = next_permut(ind1, pool) # печатает следующую перестановку        

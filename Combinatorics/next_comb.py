### Решение задачи из раздела 1.4 курса "Основы перечислительной комбинаторики"
### на stepik.org

## Задача: Нужно сгенерировать все возможные k-сочетания из n элементов.
##
## Формат входных данных:
## Два числа k и n через пробел.
## Для них гарантированно выполняется условие: 0 <= k <= n. 
##
## Формат выходных данных:
## Необходимое число строк, в каждой из которых содержится k чисел
## из диапазона от 0 до n-1 включительно, разделенных пробелом.


def next_comb(ind, n):
    """
    Функция, которая выводит на экран и возвращает массив из k чисел,
    следующих за данным массивом в порядке перечисления. Например, для массива
    (1, 2, 4) и n = 5 будет возвращено (1, 2, 5)
    """

    k = len(ind)
    for i in reversed(range(0,k)):
        if ind[i] < n - k + i:
                ind[i]+=1
                for j in range(i+1, k):
                    ind[j] = ind[j-1] + 1                
                print(*ind)
                return ind

def comb(k,n):
    """
    Функция, которая выводит все k сочетания из n чисел от 0 до n - 1
    """

    if k == 1:
        for i in range(0,n):
            print(i)
    elif k == n and k != 0:
        for i in range(0,k):
            print(i, end=' ')
    elif k > 1 and k < n:
        pool = [i for i in range(0,n)]
        ind1 = [i for i in range(0,k)]
        print(*ind1)
        ind2 = [i for i in range(n-k,n)]
        while ind1 != ind2:
                ind1 = next_comb(ind1, n)        

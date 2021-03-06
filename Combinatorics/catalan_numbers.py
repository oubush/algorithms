### Решение задачи из раздела 3.4 курса "Основы перечислительной комбинаторики"
### на stepik.org

## Задача: На вход подается единственное натуральное число n≤1000. Вам нужно
## вычислить число Каталана Cn. Так как оно может быть очень большим,
## выведите его по модулю 1000000007.

## Sample Input:
## 766

## Sample Output:
## 877790221

##n = int(input())
##def Cat_n(n):
##    C = 0
##    if n == 0:
##        return 1
##    else:
##        for k in range(1,n+1):
##            C+= Cat_n(k-1)*Cat_n(n-k)
##        return C 

N = int(input())
C = [0 for i in range(0,N+1)]
C[0]=1
n = 1
while n < N+1:
    for k in range(1,n+1):
        C[n]+=C[k-1]*C[n-k]
    n+=1

print(C[N]%1000000007)

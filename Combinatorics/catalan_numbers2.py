### Решение задачи из раздела 3.4 курса "Основы перечислительной комбинаторики"
### на stepik.org

## Задача: Зная явный вид чисел Каталана, выведите рекуррентное соотношение,
## выражающее C(n+1) только через Cn и используйте его для эффективного
## вычисления Cn. На вход подаётся число n≤100000. Выведите Cn по модулю 1000000007.

## Sample Input:
## 79172

## Sample Output:
## 30408719

##n = int(input())
##def Cat_n(n):
##    C = 0
##    if n == 0:
##        return 1
##    else:
##        for k in range(1,n+1):
##            C+= Cat_n(k-1)*Cat_n(n-k)
##        return C 

##N = int(input())
##C = [0 for i in range(0,N+1)]
##C[0]=1
##n = 1
##while n < N+1:
##    for k in range(1,n+1):
##        C[n]+=C[k-1]*C[n-k]
##    n+=1
##
##print(C[N]%1000000007)

##def fastExp(b, n):
##    def even(n):#проверка четности
##        if n%2==0:
##            return 1
##        return 0
##    if n==0:
##        return 1
##    if even(n):
##        return fastExp(b, n/2)**2
##    return b*fastExp(b, n-1)
 
##N = int(input())
### C = [0 for i in range(0, N+1)]
##C = 1
##K = 0
##R = 1
##n = 1
##D = 1000000007
##while n < N+1:
##    
##    # C = (4 * n - 2) * C / (n + 1)
##    C = (K * D + R)
##    K = ((4 * n - 2) * C / (n + 1)) // D
##    R = ((4 * n - 2) * C / (n + 1)) % D
##    
##    n += 1
##print(n, int(R))

# FIXME: нужно как-то делить по модулю после каждой операции


a = 42

p = 1000000007

b = 5

print(a%b)
print(a*b**(p-2)%p)

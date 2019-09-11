def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False
    is_prime[1] = False
    
    for i in range(2, n+1):
        if is_prime[i]:
            j = 2 * i
            while j <= n:
                is_prime[j] = False
                j += i
    table = [ i for i in range(n+1) if is_prime[i]]
    return table, is_prime

N = int(input())
L = [list(map(int, input().split())) for _ in range(N)]

prime, flag = sieve(10 ** 5)
number = [0 for i in range(10 ** 5+1)]

for i in range(2, 10 ** 5):
    if flag[i] and flag[(i+1)//2]:
        number[i] += 1
        
for i in range(1, 10 ** 5):
    number[i] += number[i-1]
        
result = []
            
for i in range(N):
    res = number[L[i][1]] - number[L[i][0]-1]
    result.append(res)

for res in result:
    print(res)

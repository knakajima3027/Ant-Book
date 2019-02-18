N = int(input())

def prime_factor(n):
    table = [0 for i in range(1000)]
    
    for x in range(2, N+1):
        for i in range(2, x+1):
            if i * i > x:
                break
            while x%i == 0:
                table[i] += 1
                x = x // i

        if x > 1:
            table[x] += 1
    return table
    
count = 1
    
res = prime_factor(N)

for r in res:
    count *= (r + 1)
    count %= 10**9+7
    
print(count)



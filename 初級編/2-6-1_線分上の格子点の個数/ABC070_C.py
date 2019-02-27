#a,bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

#a,bの最小公倍数
def lcm(a, b):
    return a * b // gcd (a, b)

N = int(input())
L = [int(input()) for _ in range(N)]

tmp = L[0]
for i in range(1, N):
    tmp = lcm(tmp, L[i])
    
print(tmp)



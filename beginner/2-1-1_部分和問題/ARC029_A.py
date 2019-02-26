N = int(input())
L = [int(input()) for _ in range(N)]

import itertools

#n桁のm値のbitを生成
def bit(n, m):
    bit_list = list(itertools.product([i for i in range(m)], repeat=n))
    return bit_list

bit = bit(4, 2)
res = 10 ** 9

for b in bit:
    tmp1 = 0
    tmp2 = 0
    for i in range(N):
        if b[i] == 0:
            tmp1 += L[i]
        else:
            tmp2 += L[i]
            
    res = min(max(tmp1, tmp2), res)
            
print(res)


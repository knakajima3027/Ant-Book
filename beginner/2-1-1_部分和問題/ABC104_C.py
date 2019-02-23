import itertools

D, G = map(int, input().split())
L = [list(map(int, input().split())) for _ in range(D)]

num = D #生成するビット数
bit_list = list(itertools.product([0, 1], repeat=num))
tmp = 10 ** 6

for bit in bit_list:
    count = 0
    num = 0
    for i in range(D):
        if bit[i] == 1:
            count += L[i][0] *(i+1) * 100 + L[i][1]
            num += L[i][0]
            
    if count >= G:
        tmp = min(num, tmp)
        
    else:
        for i in range(1, D+1):
            if bit[D-i] == 0:
                for j in range(L[D-i][0]):
                    count += (D-i+1) * 100
                    num += 1
                    if count >= G:
                        break
                break
                
        if count >= G:
            tmp = min(num, tmp)
            
print(tmp)

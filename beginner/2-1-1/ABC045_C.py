import itertools

S = input()

seq = (0, 1)
ptr = itertools.product(seq, repeat=len(S)-1)
res = 0 

for p in ptr:
    tmp = 0
    tmps = S[0]
    
    for i in range(len(S)-1):
        if p[i] == 0:
            tmps += S[i+1]
        else:
            tmp += int(tmps)
            tmps = S[i+1]
            
    if tmps != '':
        tmp += int(tmps)     
        
    res += tmp
     
print(res)

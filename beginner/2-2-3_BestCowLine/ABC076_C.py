S = input()
T = input()


tmp = -1
for i in range(len(S) - len(T) + 1):
    start = -1
    for j in range(len(T)):
        if S[i+j] == T[j] or S[i+j] == '?':
            start = i
        else:
            start = -1
            break
                       
    if start != -1:
                tmp = i
if tmp == -1:
    print('UNRESTORABLE')
    
else:
    res = ''
    count = 0
    for i in range(len(S)):
        if tmp <= i < tmp + len(T):
            res += T[count]
            count += 1
            
        elif S[i] == '?':
            res += 'a'
            
        else:
            res += S[i]

    print(res)

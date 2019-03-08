T = int(input())
S = [input() for _ in range(T)]


for i in range(T):
    j = 0
    res = 0
    while True:
        if j <= len(S[i]) - 5:
            if S[i][j] ==  'k' and S[i][j+1] == 'y' and S[i][j+2] == 'o' and S[i][j+3] == 't' and S[i][j+4] == 'o':
                res += 1
                j += 5
            elif S[i][j] ==  't' and S[i][j+1] == 'o' and S[i][j+2] == 'k' and S[i][j+3] == 'y' and S[i][j+4] == 'o':
                res += 1
                j += 5
            else:
                j += 1
        else:
            j += 1
   
        if j == len(S[i]):
            print(res)
            break

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

A.sort(key=lambda x: x[0], reverse=True)
B.sort(key=lambda x: x[1])


flag1 = [False for _ in range(N)]
flag2 = [False for _ in range(N)]

res = 0
for i in range(N):
    for j in range(N):
        if A[i][0] < B[j][0] and A[i][1] < B[j][1] and flag1[i] == False and flag2[j] == False:
            res += 1
            flag1[i] = True
            flag2[j] = True

print(res)



T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

if N < M:
    print("no")
else:
    tmp = 0
    res = "no"
    for i in range(N):
        if A[i] <= B[tmp] <= A[i] + T :
            tmp += 1
            
        if tmp == M:
            res = "yes"
            break
    print(res)
        


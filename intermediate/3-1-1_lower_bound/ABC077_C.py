import bisect

N = int(input())
A = list(map(int, input().split())) 
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

res = 0
for b in B:
    res += bisect.bisect_left(A, b) * (N - bisect.bisect_right(C, b))

print(res)



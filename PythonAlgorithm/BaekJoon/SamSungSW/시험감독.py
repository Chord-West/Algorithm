import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

import sys
input = sys.stdin.readline

N = int(input()) # 시험장의 개수
A = list(map(int,input().split())) # 시험장에 있는 응시자의 수
B,C = map(int,input().split())
ans = len(A)
A = [a-B for a in A]

for i in range(len(A)):
    if A[i]>0:
        if A[i]%C==0:
            ans+=A[i]//C
       else:
            ans += A[i] // C + 1

print(ans)
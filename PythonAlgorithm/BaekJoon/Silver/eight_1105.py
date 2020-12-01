import sys

sys.stdin = open("input.txt","rt")

A, B = map(str,input().split(' '))

count = 0


if len(A) != len(B):
    print(0)
else:     
    for i in range(len(A)):
       if A[i] == B[i]:
           if A[i] == '8':
               count += 1
           else:
              break

   
print(count)
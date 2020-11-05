import sys
#sys.stdin = open("input.txt","rt")


def isPrime(x):
    ch=1
    if check[x]==0:
        ch=0
    return ch


def reverse(x):
    res=0
    while x!=0:
        n=x%10
        res=res*10+n
        x=int(x/10)
    return res

n = int(input())
k = list(map(int,input().split()))
check=[0]*(100000)
check[1]=1

for i in range(2,100000):
    if check[i]==0:
        for j in range(i+i,100000,i):
            check[j]=1


for i in range(n):
    num=reverse(k[i])
    if(isPrime(num)==0):
        print(num,end=' ')



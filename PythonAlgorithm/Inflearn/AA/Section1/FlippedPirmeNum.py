import sys
sys.stdin = open("input.txt","rt")


def isPrime(x):
    if x==1:
        return False
    for i in range(2, x//2+1):
        if x%i==0:
            return False
    else:
        return True


def reverse(x):
    res=0
    while x>0:
        n=x%10
        res=res*10+n
        x=x//10
    return res

n = int(input())
k = list(map(int,input().split()))
check=[0]*(100000)
check[1]=1

for i in range(2,100000):
    if check[i]==0:
        for j in range(i+i,100000,i):
            check[j]=1


for x in k:
    num=reverse(x)
    if isPrime(num):
        print(num,end=' ')



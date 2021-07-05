import sys
from math import pow
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

a,b,c = map(int,input().split())

def divide(a,b):

    if b==1:
        return a%c
    elif b==2:
        return a*a%c
    else:
        tmp = divide(a,b//2)
        if b%2==0:
            return tmp*tmp%c
        else:
            return tmp*tmp*a%c

answer = divide(a,b)
print(answer)
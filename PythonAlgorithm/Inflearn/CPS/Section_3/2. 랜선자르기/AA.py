import sys
#sys.stdin = open("input.txt","rt")

if __name__ =="__main__":
    k,n=map(int,input().split())
    line=[int(input()) for _ in range(k)]
    g=sum(line)//n
    ch=0
    mid=g
    lt,rt=0,g
    max=0
    while lt<=rt:
        mid=(lt+rt)//2
        for x in line:
            ch += x // mid
        if ch<n:
            rt=mid-1
        elif ch>=n:
            lt=mid+1
            if mid>max:
                max=mid
        ch=0
    print(max)
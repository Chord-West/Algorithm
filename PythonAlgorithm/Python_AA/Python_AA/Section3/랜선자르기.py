import sys
sys.stdin = open("input.txt","rt")

def Count(len):
    cnt=0
    for x in line:
        cnt+=(x//len)
    return cnt

if __name__ =="__main__":
    k,n=map(int,input().split())
    line=[int(input()) for _ in range(k)]
    line.sort()
    res=0
    lt,rt=0,line[k-1]
    while lt<=rt:
        mid=(lt+rt)//2
        if Count(mid)>=n:
            res=mid
            lt=mid+1
        else:
            rt=mid-1
    print(res)
import sys
#sys.stdin = open("input.txt","r")

def Count(L):
    cnt=1
    sum=0
    for i in range(1,n):
        sum+=ma[i]-ma[i-1]
        if sum>=L:
            cnt+=1
            sum=0
    return cnt


if __name__ == "__main__":
    n,c = map(int,input().split())
    ma = [int(input()) for _ in range(n)]
    ma.sort()
    lt,rt=1,ma[n-1]
    ans=0
    while(lt<=rt):
        mid=(lt+rt)//2
        if Count(mid)>=c:
            lt=mid+1
            ans=mid
        else:
            rt=mid-1
    print(ans)
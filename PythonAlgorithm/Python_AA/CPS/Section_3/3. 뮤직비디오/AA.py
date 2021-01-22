import sys
#sys.stdin = open("input.txt","rt")

def Count(L):
    cnt=0
    sum=0
    for x in movies:
        sum+=x
        if L<sum:
            cnt+=1
            sum=x
    else:
        if sum>0:
            cnt+=1
    return cnt



if __name__ == "__main__":
    n,m=map(int,input().split())
    movies = list(map(int,input().split()))
    total=sum(movies)
    lt,rt=1,total
    ans=0
    while(lt<=rt):
        mid=(lt+rt)//2
        if Count(mid)<=m:
            rt=mid-1
            ans=mid
        else:
            lt=mid+1
    print(ans)
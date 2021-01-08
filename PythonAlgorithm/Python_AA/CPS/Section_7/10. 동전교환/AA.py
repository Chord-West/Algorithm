#import sys
#sys.stdin = open("input.txt", "rt")
'''
if __name__ == "__main__":
    n = int(input())
    coin = list(map(int,input().split()))
    m = int(input())
    dp=[1000]*(m+1)
    dp[0]=0
    
    for c in coin:
        for i in range(c,m+1):
            dp[i]=min(dp[i],dp[i-c]+1)

    print(dp[m])
'''

if __name__ == "__main__":
    n = int(input())
    coin = list(map(int, input().split()))
    coin.sort(reverse=True)
    m = int(input())
    idx=0
    ans=0
    while m!=0 :
        if m-coin[idx]>=0:
            m-=coin[idx]
            ans+=1
        else:
            idx+=1

    print(ans)
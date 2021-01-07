#import sys
#sys.stdin = open("input.txt","rt")

if __name__ == '__main__':
    n ,m = map(int,input().split())
    # 0 무게 , 1 가치
    jew = [list(map(int,input().split()))for _ in range(n)]
    #가치가 높은 순으로
    dp=[0]*(m+1)
    for w,v in jew:
        for i in range(w,m+1):
            dp[i]=max(dp[i],dp[i-w]+v)

    print(dp[m])
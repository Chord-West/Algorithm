#import sys
#sys.stdin = open("input.txt","rt")

if __name__=="__main__":
    n = int(input())
    bridge = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0]*n for _ in range(n)]
    dp[0][0] = bridge[0][0]

    for i in range(n):
        dp[0][i]=dp[0][i-1]+bridge[0][i]
        dp[i][0] = dp[i-1][0] + bridge[i][0]


    for i in range(1,n):
        for j in range(1,n):
            dp[i][j]=min(dp[i][j-1],dp[i-1][j])+bridge[i][j]


    print(dp[n-1][n-1])
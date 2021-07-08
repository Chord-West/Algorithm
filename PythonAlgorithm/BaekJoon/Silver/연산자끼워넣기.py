import sys
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline

def dfs(L,S):
    global max_ans,min_ans
    if L==n-1:
        max_ans = max(S,max_ans)
        min_ans = min(S,min_ans)
    else:
        for i in range(len(oper)):
            if oper[i]>0:
                oper[i]-=1
                if i==0:
                    dfs(L + 1,S+nums[L+1])
                elif i==1:
                    dfs(L + 1, S - nums[L + 1])
                elif i==2:
                    dfs(L + 1, S * nums[L + 1])
                else:
                    if S<0:
                        dfs(L + 1, -(abs(S) //nums[L + 1]))
                    else:
                        dfs(L + 1, S // nums[L + 1])

                oper[i]+=1

n = int(input())
nums=list(map(int,input().split()))
oper=list(map(int,input().split()))
min_ans,max_ans=sys.maxsize,-sys.maxsize
dfs(0,nums[0])
print(max_ans)
print(min_ans)


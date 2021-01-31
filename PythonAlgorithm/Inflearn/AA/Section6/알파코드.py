import sys
sys.stdin = open("input.txt","rt")

def dfs(L,P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            print(chr(64+ans[j]),end='')
        print()
    else:
        for i in range(1,27):
            if num[L]==i:
                ans[P]=i
                dfs(L+1,P+1)
            elif i>=10 and num[L]==i//10 and num[L+1]==i%10:
                ans[P]=i
                dfs(L+2,P+1)


if __name__ == "__main__":
    num = list(map(int,input()))
    n=len(num)
    num.append(-1)
    ans=[0]*(n)
    cnt=0
    dfs(0,0)
    print(cnt)

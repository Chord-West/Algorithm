import sys
from itertools import combinations
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline


def make_team(L,idx):
    global ans
    if L == N//2:
        start = []
        link = []
        for i in range(1,N+1):
            if visited[i] == 1:
                start.append(i)
            else:
                link.append(i)
        ans = min(ans,find_score(start,link))
        return
    else:
        for i in range(1,N+1):
            if visited[i]==0 and i > idx:
                visited[i]=1
                make_team(L+1,i)
                visited[i]=0

def find_score(start,link):
    s_score = 0
    l_score = 0
    for a,b in list(combinations(start,2)):
        s_score += team[a-1][b-1]
        s_score += team[b-1][a-1]
    for c,d in list(combinations(link,2)):
        l_score += team[c-1][d-1]
        l_score += team[d-1][c-1]
    return abs(s_score-l_score)

ans = 999999
N = int(input())
team = [list(map(int,input().split())) for _ in range(N)]
visited = [0]*(N+1)
visited[1]=1

make_team(1,1)
print(ans)



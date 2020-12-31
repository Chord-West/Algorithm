#import sys
#sys.stdin = open("input.txt","rt")

n = int(input())
player=[list(map(int,input().split())) for _ in range(n)]

player.sort(key=lambda x:x[0], reverse=True)

max=0
sum=0
for h,w in player:
    if w>max:
        max=w
        sum+=1

print(sum)
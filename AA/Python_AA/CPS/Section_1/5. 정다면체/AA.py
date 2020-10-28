import sys
#sys.stdin=open("input.txt","rt")

n,m= map(int, input().split())
list = []
answer=[]
for i in range(n+m+1):
    list.append(0)

for i in range(1,n+1):
    for j in range(1,m+1):
        list[i+j]+=1 

max = -2147000000
for i in range(len(list)):
    if(list[i]>max):
        max=list[i]

for idx ,x in enumerate(list):
    if x == max:
       print(idx,end=' ')


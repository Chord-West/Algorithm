import sys

#sys.stdin = open("input.txt","rt")

n,k = map(int,input().split())
num = list(map(int,input().split()))
res = set() # 중복을 없애는 자료구조
for i in range(n):
    for j in range(i+1,n):
        for m in range(j+1,n):
            res.add(num[i]+num[j]+num[m]) 

res = list(res) #set은 sort가 없음
res.sort(reverse=True)
print(res[k-1])


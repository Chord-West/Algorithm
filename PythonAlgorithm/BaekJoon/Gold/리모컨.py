import sys
sys.stdin = open("input.txt","rt")

remote = {x for x in range(10)}
n = int(input())
m = int(input())
if m!=0:
    remote-=set(map(int,input().split()))
min_cnt = abs(100-n)

for i in range(1000001):
    ch = True
    for num in str(i):
        print(num)
        if num not in remote:
            ch = False
            break
    if ch:
        min_cnt = min(min_cnt,abs(n-i)+len(str(i)))
print(min_cnt)



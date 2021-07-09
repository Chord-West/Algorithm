import sys
from collections import defaultdict
sys.stdin = open("input.txt","rt")
input = sys.stdin.readline


N,K = map(int,input().split())
p = defaultdict(int)
if K <5: # 5아래일때에는 읽을수 있는게 없다
    print(0)
    exit(0)
letters=['a','n','t','i','c']
words=[]
for _ in range(N):
    tmp = input().rstrip('\n')
    words.append(tmp)
    tmp_letters=set()
    for char in tmp[4:len(tmp)-4]:
        if char in letters:
            pass
        else:
            tmp_letters.add(char)
    for t in tmp_letters:
        p[t]+=1
print(p)
most_letters=sorted(p.keys(),key=lambda x:p[x],reverse=True)[:K-5]
letters.extend(most_letters)
ans=0
for word in words:
    for char in word:
        if char not in letters:
            break
    else:
        ans+=1
print(ans)
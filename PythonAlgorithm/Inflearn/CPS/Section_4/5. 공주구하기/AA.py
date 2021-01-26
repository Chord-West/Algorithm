#import sys
#sys.stdin = open("input.txt","r")

if __name__ == "__main__":
    n,m = map(int,input().split())
    p = [i+1 for i in range(n)]
    count=0
    x=0
    while p:
        count+=1
        if count==m:
            p.pop(0)
            count=0
        else:
            x=p.pop(0)
            p.append(x)
    print(x)
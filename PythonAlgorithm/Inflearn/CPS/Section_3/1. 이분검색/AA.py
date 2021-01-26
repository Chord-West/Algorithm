#import sys
#sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    n,m = map(int,input().split())
    num = list(map(int,input().split()))
    num.sort()

    lt,rt=0,len(num)-1
    while lt<=rt:
        mid = (lt+rt) // 2
        if num[mid] == m:
            print(mid+1)
            break
        elif num[mid]>m:
            rt=mid-1
        else:
            lt=mid+1
#import sys
#sys.stdin = open("input.txt","rt")

if __name__ =="__main__":
    n = int(input())
    words=[ input() for _ in range(n)]
    words2=[input() for _ in range(n-1)]
    for x in words:
        if x not in words2:
            print(x)

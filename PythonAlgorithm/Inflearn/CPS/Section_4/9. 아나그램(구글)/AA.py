#import sys
#sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    p=dict()
    s=dict()
    for w in input():
        p[w]=p.get(w,0)+1
    for w2 in input():
        s[w2]=s.get(w2,0)+1
    if p==s:
        print("YES")
    else:
        print("NO")
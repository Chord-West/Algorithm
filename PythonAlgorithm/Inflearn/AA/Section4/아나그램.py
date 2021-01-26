import sys
sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    p=dict()
    for w in input():
        p[w]=p.get(w,0)+1
    for w in input():
        p[w]=p.get(w,0)-1
    for key,value in p.items():
        if value>0:
            print("NO")
            break
    else:
        print("YES")
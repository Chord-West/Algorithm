import sys
sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    s = [x for x in input()]
    n = int(input())
    ans=[]
    for i in range(n):
        for x in input():
            if x in s:
                ans.append(x)
        if ans==s:
            print("#{} YES".format(i+1))
        else:
            print("#{} NO".format(i + 1))
        ans.clear()

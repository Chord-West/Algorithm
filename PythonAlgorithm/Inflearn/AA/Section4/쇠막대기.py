import sys
sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    stack=[]
    sum=0
    y='' # 한개전수
    for x in input():
        if x=='(':
            stack.append(x)
        elif x==')':
            if y =='(':
                stack.pop()
                sum+=len(stack)
            else:
                stack.pop()
                sum+=1
        y=x
    print(sum)


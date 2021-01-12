#import sys
#sys.stdin = open("input.txt","rt")

if __name__ == "__main__":
    stack=[]
    for x in input():
        if x.isdigit():
            stack.append(int(x))
        else:
            sum=0
            a=stack.pop()
            b=stack.pop()
            if x=='*':
                sum=b*a
            elif x=='/':
                sum = b / a
            elif x == '+':
                sum = b + a
            elif x == '-':
                sum = b- a
            stack.append(sum)

    print(stack.pop())
from collections import deque

def cal(start,end,idx):
    stack=[]
    result = 0
    max_h = 0
    for i in range(start,end,idx):
        if height[i]>=max_h:
            while stack:
                result+=max_h-height[stack.pop()]
            max_h=height[i]
        else:
            stack.append(i)
    return result
height = [4,2,0,3,2,5]
answer = 0
mid = height.index(max(height))
answer+=cal(0,mid+1,1)
answer+=cal(mid-1,0,-1)

for i in range(len(height)-1,mid-1,-1):
    print(i)

print(answer)
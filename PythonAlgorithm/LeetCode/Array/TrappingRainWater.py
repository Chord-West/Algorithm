from collections import deque

height = [0,1,0,2,1,0,1,3,2,1,2,1]
stack = []
answer = 0

for i in range(len(height)):
    while stack and height[i] > height[stack[-1]]:
    # 스탹에서 꺼낸다
        top = stack.pop()
        if not len(stack):
            break
        distance = i - stack[-1] -1
        waters = min(height[i],height[stack[-1]]) - height[top]

        answer+= distance*waters

    stack.append(i)


print(answer)
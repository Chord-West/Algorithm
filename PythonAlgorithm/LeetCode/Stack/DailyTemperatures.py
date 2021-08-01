def dailyTemperatures(T):
    ans=[0] * len(T)
    stack=[]
    for i, t in enumerate(T):
        # 현재 온도가 스택큐 값보다 높다면 정답처리
        while stack and t>T[stack[-1]]:
            last = stack.pop()
            ans[last] = i -last
        stack.append(i)
    return ans

dailyTemperatures([73,74,75,71,69,72,76,73])
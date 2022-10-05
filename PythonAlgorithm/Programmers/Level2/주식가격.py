def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            x = stack.pop()
            answer[x] = i - x
        stack.append(i)
    while stack:
        y = stack.pop()
        answer[y] = len(prices) - y - 1

    return answer
def solution(prices):
    answer = [0] * len(prices)
    stack = []

    for idx, price in enumerate(prices):
        while stack and stack[-1][0] > price:
            p, i = stack.pop()
            answer[i] = idx - i
        stack.append((price, idx))
    if stack:
        x = stack.pop()
        while stack:
            y = stack.pop()
            answer[y[1]] = x[1] - y[1]
    return answer
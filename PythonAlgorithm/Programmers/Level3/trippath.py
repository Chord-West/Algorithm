from collections import defaultdict

def solution(tickets):

    def dfs(start):
        stack=[start]
        path=[]
        while stack:
            top = stack[-1]
            if top not in routes or len(routes[top]) ==0:
                path.append(stack.pop())
            else:
                stack.append(routes[top].pop(0))
        return path[::-1]

    start = "ICN"
    routes = defaultdict(list)  # dictionary 이용해서 인접리스트구하기
    for key, value in tickets:
        routes[key].append(value)

    for x in routes:
        routes[x].sort()
    answer= dfs(start)
    return answer









tickets=[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
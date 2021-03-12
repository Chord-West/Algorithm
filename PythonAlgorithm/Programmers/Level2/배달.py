def solution(N, road, K):
    answer = 0

    def dfs(L, S):
        if S <= K:
            print(L)
            ch[L] = 1
        if S > K:  # 배달 시간 넘어갈경우
            return
        else:
            for x in graph[L]:
                if ch[x[0]] == 0:
                    dfs(x[0], S + x[1])  # x[0]은 마을번호 , x[1은 시간]

    graph = [[] for _ in range(N + 1)]
    ch = [0] * (N + 1)
    for x in road:
        graph[x[0]].append([x[1], x[2]])
        graph[x[1]].append([x[0], x[2]])
    dfs(1, 0)
    print(graph)
    print(ch)
    return answer

solution(5,[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]],3)
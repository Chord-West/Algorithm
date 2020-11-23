# 각 노드가 연결된 정보를 표현 ( 2차원 리스트 )
graph = [
    [], # 보통 인덱스는 1번부터 시작해서 비워둠
    [2,3,8], # 1번이 연결된 노드들
    [1,7],
    [1,4,5,],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

def dfs(graph,v,visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph,1,visited)

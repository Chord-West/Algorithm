from collections import deque

# BFS 메서드 정의

def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    
    visited[start] = True

    while queue:
        # 큐에서 하나의 원소를 뽑아 출력하기
        v = queue.popleft()
        print(v , end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


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

bfs(graph,1,visited)

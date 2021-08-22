def solution(routes):
    answer = 0
    n = len(routes)
    routes.sort(key=lambda x: x[1])
    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:
            camera = routes[i][1]
            answer += 1
        for j in range(i + 1, n):
            if routes[j][0] <= camera <= routes[j][1] and visited[j] == 0:
                visited[j] = 1

    return answer
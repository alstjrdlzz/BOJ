from collections import deque


n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)
 
def bfs(graph, start):
    visited = [0 for _ in range(len(graph))]
    answer = [0 for _ in range(len(graph))]
    queue = deque([start])
    visited[start] = 1
    while queue:
        parent = queue.popleft()
        for child in graph[parent]:
            if visited[child] == 0:
                visited[child] = 1
                answer[child] = parent
                queue.append(child)
    return answer

answer = bfs(graph, 1)

for i in range(2, n+1):
    print(answer[i])
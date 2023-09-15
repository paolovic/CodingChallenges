def bfs(n, m, edges, s):
    # Write your code here
    graph = {}
    for i in range(1, n + 1):
        graph[i] = set()
    for i in range(m):
        graph[edges[i][0]].add(edges[i][1])
        graph[edges[i][1]].add(edges[i][0])

    queue = [s]
    visited = set()
    result = [-1] * (n - 1)
    run = 0

    while len(queue) > 0:
        for i in range(len(queue)):
            node = queue.pop(0)
            visited.add(node)
            if node != s:
                if node < s:
                    result[node - 1] = 6 * run
                else:
                    result[node - 2] = 6 * run
            neighbors = graph[node]
            for n in neighbors:
                if n not in visited:
                    queue.append(n)
        run += 1

    return result


n = 10
m = 6
edges = [[3, 1], [10, 1], [10, 1], [3, 1], [1, 8], [5, 2]]
s = 3
print(bfs(n, m, edges, s))  # [6, 6, 12, 12, -1, 6, 6, 12, 12]

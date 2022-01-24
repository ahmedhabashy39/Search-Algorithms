graph = {
    'a': ['d', 'b'],
    'b': ['e'],
    'd': ['f'],
    'e': ['g', 'c'],
    'f': ['c', 'g'],
    'c': ['g', 'a'],
    'g': []
}


def BFS(graph, start, goal=None):
    queue = [start]
    visited = []
    while queue:
        vertex = queue.pop(0)
        visited.append(vertex)
        if vertex == goal:
            return visited
        for neighbor in graph[vertex]:
            if neighbor not in visited+queue:
                queue.append(neighbor)
    return visited


print("BFS: ", BFS(graph, 'a', 'g'))


def DFS(graph, start, goal=None):
    stack = [start]
    visited = []
    while stack:
        vertex = stack.pop()
        visited.append(vertex)
        if vertex == goal:
            return visited

        stack.extend(graph[vertex])
    return visited


print("DFS: ", DFS(graph, 'a', 'g'))

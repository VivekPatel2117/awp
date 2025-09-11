from collections import deque

def dfs(graph, start, target=None, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(f"Visited: {start}")
        visited.add(start)

        if start == target:
            print(f"Target '{target}' found")
            return True

        for neighbor in graph.get(start, []):
            if neighbor not in visited:
                if dfs(graph, neighbor, target, visited):
                    return True

    return False if target else True


# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6],
    4: [],
    5: [6],
    6: []
}

print("DFS traversal:")
dfs(graph, 1, target=7)

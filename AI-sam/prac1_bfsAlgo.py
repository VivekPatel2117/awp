from collections import deque

def bfs(graph, start, target=None):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if node not in visited:
            print(f"Visited: {node}")
            visited.add(node)

            if node == target:
                print(f"Target '{target}' found")
                return True

            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

    if target:
        print(f"Target '{target}' not found in the graph.")
        return False
    
    return True


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
    '0': ['1', '2'],
    '1': ['3', '4'],
    '2': ['5'],
    '3': ['6'],
    '4': ['7'],
    '5': []
}
print("BFS traversal:")
bfs(graph, '0', target='7')

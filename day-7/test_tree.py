from collections import deque


def findPaths(edges, src, dest):
    graph = {}

    # Build the graph from edges
    for edge in edges:
        if edge[0] not in graph:
            graph[edge[0]] = []
        graph[edge[0]].append(edge[1])

    allPaths = []
    q = deque()

    # Initialize queue with the starting path
    q.append([src])

    while q:
        path = q.popleft()
        current = path[-1]

        # If destination is reached, store the path
        if current == dest:
            allPaths.append(path)

        # Explore all adjacent vertices
        if current in graph:
            for adj in graph[current]:
                newPath = list(path)
                newPath.append(adj)
                q.append(newPath)

    return allPaths


if __name__ == "__main__":
    edges = [
        [17, 26],
        [26, 35],
        [44, 53],
        [53, 84],
        [53, 62],
        [62, 71],
        [71, 80],
        [71, 82],
        [62, 73],
        [73, 82],
        [73, 84],
        [35, 44],
    ]
    src = 17
    dest = 84

    paths = findPaths(edges, src, dest)
    print(len(paths))

    for path in paths:
        for vtx in path:
            print(vtx, end=" ")
        print()

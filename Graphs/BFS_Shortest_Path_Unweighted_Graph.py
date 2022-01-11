import collections

def shortestPathBFS(graph, source):
    # initialize the distance table
    distanceTable = {vertex:(None, -1) for vertex in graph}

    queue = collections.deque()
    queue.append((None, source, -1)) # (from, to, distance)


    while queue:
        fromVertex, toVertex, distance = queue.popleft()

        if distanceTable[toVertex][1] == -1:
            distance += 1
            distanceTable[toVertex] = (fromVertex, distance)
        
            if graph[toVertex]:
                for neighbor in graph[toVertex]:
                    queue.append((toVertex, neighbor, distance))

    return distanceTable


def shortestPathToBFS(graph, source, destination):
    # initialize the distance table
    distanceTable = {vertex:(None, -1) for vertex in graph}

    queue = collections.deque()
    queue.append((None, source, -1)) # (from, to, distance)

    while queue:
        fromVertex, toVertex, distance = queue.popleft()

        if distanceTable[toVertex][1] == -1:
            distance += 1
            distanceTable[toVertex] = (fromVertex, distance)

            if toVertex==destination:
                return distance

            if graph[toVertex]:
                for neighbor in graph[toVertex]:
                    queue.append((toVertex, neighbor, distance))

    return -1   

def getPath(graph, source, destination):
    distanceTable = shortestPathBFS(graph, source)

    if distanceTable[destination][1] == -1:
        return []
    else:
        path = []
        current = destination
        while current != source:
            path.append(current)
            current = distanceTable[current][0]
        path.append(source)
        path.reverse()
        return path
    
if __name__ == "__main__":
    graph = {
    'A': ['B', 'D'],
    'B': ['D', 'E'],
    'C': ['A', 'F'],
    'D': ['F', 'G'],
    'E': ['G'],
    'F': None,
    'G': ['F']
    }

    print(getPath(graph, 'C', 'G'))
    print(shortestPathBFS(graph, 'C'))
    print(shortestPathToBFS(graph, 'C', 'D'))
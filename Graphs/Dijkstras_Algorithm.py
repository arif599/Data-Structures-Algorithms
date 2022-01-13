def dijkstras(graph, source):
    import heapq
    import math
    distanceTable = {vertex:math.inf for vertex in graph}
    distanceTable[source] = 0
    minPriorityQueue = [(0, None, source)]

    while minPriorityQueue:
        distance, fromVertex, toVertex = heapq.heappop(minPriorityQueue)

        if distance > distanceTable[toVertex]:
            continue

        for neighbor in graph[toVertex]:
            newDistance = distance + graph[toVertex][neighbor]
            if newDistance < distanceTable[neighbor]:
                distanceTable[neighbor] = newDistance
                heapq.heappush(minPriorityQueue, (newDistance, toVertex, neighbor))

    return distanceTable


if __name__ == "__main__":
    graph = {
        'A': {'B': 5, 'C': 1},
        'B': {'A': 5, 'C': 2, 'D': 1},
        'C': {'A': 1, 'B': 2, 'D': 4, 'E': 8},
        'D': {'B': 1, 'C': 4, 'E': 3, 'F': 6},
        'E': {'C': 8, 'D': 3},
        'F': {'D': 6}
    }

    print(dijkstras(graph, 'A'))
    
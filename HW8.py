graph = {
    1: {2: 10, 3: 15, 4: 20},
    2: {1: 10, 3: 35, 4: 25},
    3: {1: 15, 2: 35, 4: 30},
    4: {1: 20, 2: 25, 3: 30}
}

start = int(input("Введите начальную вершину: "))

def tsp_nearest_neighbor(graph, start):
    current = start
    visited = {current}
    path = [current]
    total_distance = 0

    while len(visited) < len(graph):
        neighbors = graph[current]
        next_node = None
        min_distance = float('inf')
        for neighbor, distance in neighbors.items():
            if neighbor not in visited and distance < min_distance:
                next_node = neighbor
                min_distance = distance
        
        visited.add(next_node)
        path.append(next_node)
        total_distance += min_distance
        current = next_node

    total_distance += graph[current][start]
    path.append(start)
    
    return path, total_distance

path, total_distance = tsp_nearest_neighbor(graph, start)
print(path, total_distance)
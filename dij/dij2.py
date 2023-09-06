import heapq

def dijkstra(graph, start, destination):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_node == destination:
            break
        if current_dist > distances[current_node]:
            continue
        for neighbor, weight in graph[current_node]:
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    if distances[destination] == float('inf'):
        return None

    route = []
    node = destination
    while node != start:
        route.append(node)
        neighbors = [edge[0] for edge in graph[node]]
        min_distance = float('inf')
        next_node = None
        for neighbor, weight in graph[node]:
            if distances[neighbor] + weight == distances[node] and distances[neighbor] < min_distance:
                min_distance = distances[neighbor]
                next_node = neighbor
        if next_node is None or next_node in route:
            return None
        node = next_node

    route.append(start)
    route.reverse()
    return route

def get_graph_from_user():
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_edges):
        node1, node2, weight = input(f"Enter edge {i + 1} (node1 node2 weight): ").split()
        weight = int(weight)
        if node1 not in graph:
            graph[node1] = []
        if node2 not in graph:
            graph[node2] = []
        graph[node1].append((node2, weight))
        graph[node2].append((node1, weight))
    return graph

start_location = input("Enter the start location: ")
destination_location = input("Enter the destination location: ")
graph = get_graph_from_user()

optimal_route = dijkstra(graph, start_location, destination_location)

if optimal_route is None:
    print("No valid route exists from the start to the destination.")
else:
    print("Optimal Route:", ' -> '.join(optimal_route))

# OUTPUT:

# Enter the start location: a
# Enter the destination location: e
# Enter the number of edges: 7
# Enter edge 1 (node1 node2 weight): b c 4
# Enter edge 2 (node1 node2 weight): c e 6
# Enter edge 3 (node1 node2 weight): d e 4
# Enter edge 4 (node1 node2 weight): b d 2
# Enter edge 5 (node1 node2 weight): d c 5
# Enter edge 6 (node1 node2 weight): a d 7
# Enter edge 7 (node1 node2 weight): a b 3
# Optimal Route: a -> b -> d -> e

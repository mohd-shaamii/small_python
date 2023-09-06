import sys
from heapq import heapify, heappush, heappop

def dijsktra(graph, src, dest):
    inf = sys.maxsize
    node_data = {}
    for node in graph:
        node_data[node] = {'cost': inf, 'pred': []}
    node_data[src]['cost'] = 0
    visited = []
    temp = src
    for i in range(len(graph) - 1):  # Iterate until all nodes are visited
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for neighbor in graph[temp]:
                if neighbor not in visited:
                    cost = node_data[temp]['cost'] + graph[temp][neighbor]
                    if cost < node_data[neighbor]['cost']:
                        node_data[neighbor]['cost'] = cost
                        node_data[neighbor]['pred'] = node_data[temp]['pred'] + [temp]
                    heappush(min_heap, (node_data[neighbor]['cost'], neighbor))
            heapify(min_heap)
            if min_heap:
                temp = min_heap[0][1]
    
    if node_data[dest]['cost'] == inf:
        print("No path from {} to {}.".format(src, dest))
    else:
        print("Shortest Distance: " + str(node_data[dest]['cost']))
        shortest_path = ' -> '.join(node_data[dest]['pred'] + [dest])
        print("Shortest Path: " + shortest_path)

if __name__ == "__main__":
    graph = {}
    num_edges = int(input("Enter the number of edges: "))
    for i in range(num_edges):
        edge_input = input(f"Enter edge {i + 1} in the format 'node1 node2 weight': ")
        node1, node2, weight = edge_input.split()
        weight = int(weight)
        
        if node1 not in graph:
            graph[node1] = {}
        if node2 not in graph:
            graph[node2] = {}
        
        graph[node1][node2] = weight
        graph[node2][node1] = weight

    source = input("Enter the source node: ")
    destination = input("Enter the destination node: ")
    dijsktra(graph, source, destination)
"""
OUTPUT:
Enter the number of edges: 7
Enter edge 1 in the format 'node1 node2 weight': A B 3
Enter edge 2 in the format 'node1 node2 weight': B C 4
Enter edge 3 in the format 'node1 node2 weight': C E 6
Enter edge 4 in the format 'node1 node2 weight': D E 4
Enter edge 5 in the format 'node1 node2 weight': B D 2
Enter edge 6 in the format 'node1 node2 weight': D C 5
Enter edge 7 in the format 'node1 node2 weight': A D 7
Enter the source node: A
Enter the destination node: E
Shortest Distance: 9
Shortest Path: ['A', 'B', 'D', 'E'] 
"""

import networkx as nx

def get_distances(num_nodes):
    distances = {}
    for i in range(1, num_nodes+1):
        for j in range(i+1, num_nodes+1):
            distance = float(input(f"Enter the distance between node {i} and node {j}: "))
            distances[(i, j)] = distance
            distances[(j, i)] = distance
    return distances

def optimal_drilling(distances):
    G=nx.Graph()
    G.add_weighted_edges_from((i,j,distance) for (i,j),distance in distances.items())
    optimal_order = nx.approximation.traveling_salesman_problem(G,cycle=True)   
    return optimal_order

def cal_optimal_cost(drill_order,distances):
    total_cost=sum(distances[(drill_order[i],drill_order[i+1])] for i in range(len(drill_order)-1))
    return total_cost

if __name__ == "__main__":
    while True:
        num_nodes = int(input("Enter th enumber of drill holes(nodes): "))
        distances = get_distances(num_nodes)
        optimal_order = optimal_drilling(distances)
        optimal_cost = cal_optimal_cost(optimal_order,distances)
        print("Optimal order of drilling: ",optimal_order)
        print("Optimal cost of drilling: ",optimal_cost)
        try_again = input("Do you want to try again with different number of node? (yes/no):").lower()
        if try_again != "yes":
            break



# Enter th enumber of drill holes(nodes): 4
# Enter the distance between node 1 and node 2: 10
# Enter the distance between node 1 and node 3: 15
# Enter the distance between node 1 and node 4: 20
# Enter the distance between node 2 and node 3: 35
# Enter the distance between node 2 and node 4: 25
# Enter the distance between node 3 and node 4: 30
# Optimal order of drilling:  [1, 3, 4, 2, 1]
# Optimal cost of drilling:  80.0
# Do you want to try again with different number of node? (yes/no):no

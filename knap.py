def knap(weights,costs,capacity):
    num_items=len(weights)
    table=[[0]*(capacity+1) for _ in range (num_items+1)]
    for i in range(1,num_items+1):
        for j in range(1,capacity+1):
            if weights[i-1]<=j:
                table[i][j]=max(costs[i-1]+table[i-1][j-weights[i-1]],table[i-1][j])
            else:
                table[i][j]=table[i-1][j]
    selected_items=[]
    total_weight=capacity
    for i in range(num_items,0,-1):
        if table[i][total_weight]!=table[i-1][total_weight]:
            selected_items.append(i-1)
            total_weight -= weights[i-1]
    return table[num_items][capacity],selected_items

weights=input("Enter the weights :").split()
weights=[int(w) for w in weights]
costs=input("Enter the costs :").split()
costs=[int (c) for c in costs]
capacity=int(input("Enter the Capacity"))
max_profit,selected_items=knap(weights,costs,capacity)
print("Max profit : ",max_profit)
print("Selected items (index) : ",selected_items)
print("Selected weights : ",[weights[i] for i in selected_items])
print("Selected costs : ",[costs[i] for i in selected_items])



# Enter the weights :2 3 4 5
# Enter the costs :10 20 30 40
# Enter the Capacity10
# Max profit :  70
# Selected items (index) :  [3, 1, 0]
# Selected weights :  [5, 3, 2]
# Selected costs :  [40, 20, 10]

import heapq


def getMinCost(cost, compatible1, compatible2, min_compatible):
    both_clusters = [cost[i] for i in range(len(cost)) if compatible1[i] and compatible2[i]]
    only_c1 = [cost[i] for i in range(len(cost)) if compatible1[i] and not compatible2[i]]
    only_c2 = [cost[i] for i in range(len(cost)) if compatible2[i] and not compatible1[i]]

    heapq.heapify(both_clusters)
    heapq.heapify(only_c1)
    heapq.heapify(only_c2)

    total_cost = 0
    while min_compatible and both_clusters:
        total_cost += heapq.heappop(both_clusters)
        min_compatible -= 1

    while min_compatible and only_c1 and only_c2:
        total_cost += heapq.heappop(only_c1) + heapq.heappop(only_c2)

        min_compatible -= 1

    if min_compatible and (not only_c1 or not only_c2):
        return -1

    return total_cost

cost = [2, 4, 6, 5]
compatible1 = [1, 1, 1, 0]
compatible2 = [0, 0, 1, 1]
min_compatible = 2
print(getMinCost(cost, compatible1, compatible2, min_compatible))

# Test
cost = [4,8,7,3,2,9]
compatible1 = [1, 1, 1, 0,0,1]
compatible2 = [1, 1,0,1,0,0]
min_compatible = 2
print(getMinCost(cost, compatible1, compatible2, min_compatible))  # Expected 12

# Test
cost = [3,4,5,6,3,2,10]
compatible1 = [1, 1, 0,1,1, 1,0]
compatible2 = [0,0,1, 0,1,1,0]
min_compatible = 3
print(getMinCost(cost, compatible1, compatible2, min_compatible))  # Expected 13
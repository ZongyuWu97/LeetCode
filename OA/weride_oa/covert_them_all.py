def coverThemAll(distance, cost):
    # Check if there's a distance of 1, if so, that's the minimum cost we can have
   # Initialize minimum cost to a large number
    if 1 in distance:
        min_cost = cost[distance.index(1)]
    else:
        min_cost = float('inf')

    # Import the gcd function from math module
    from math import gcd
    from functools import reduce

    # Function to find gcd of a list of numbers
    def find_gcd(list):
        x = reduce(gcd, list)
        return x

    # Initialize the minimum cost to the sum of all costs as the worst case scenario
    min_cost = sum(cost)

    # Using bitmask to generate all possible combinations of distances
    n = len(distance)
    for i in range(1, 1 << n):
        selected_distances = [distance[j] for j in range(n) if (i & (1 << j))]
        # If the GCD of the selected distances is 1, they can cover all integers
        if find_gcd(selected_distances) == 1:
            current_cost = sum(cost[j] for j in range(n) if (i & (1 << j)))
            min_cost = min(min_cost, current_cost)

    # If we found a combination that can cover all integers, return the cost, otherwise -1
    return min_cost if min_cost != sum(cost) else -1

# Test the function with the provided examples
example1 = coverThemAll([1, 2, 3], [3, 1, 1])
example2 = coverThemAll([20, 10, 3], [3, 1, 1])

print(example1, example2)

distance = [1, 2, 3]
cost = [1, 2, 3]
print(coverThemAll(distance,cost))
distance = [7, 11, 3]
cost = [2, 6, 1]
print(coverThemAll(distance,cost))


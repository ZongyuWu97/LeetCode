class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        return sum([x[0] for x in costs[:len(costs) // 2]]) + sum([x[1] for x in costs[len(costs) // 2:]])
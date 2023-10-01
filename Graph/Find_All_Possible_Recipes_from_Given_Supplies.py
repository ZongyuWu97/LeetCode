class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        for recipe, ingredient in list(zip(recipes, ingredients)):
            for i in ingredient:
                graph[i].append(recipe)
                indegree[recipe] += 1
        for s in supplies:
            indegree[s] = 0
        
        q = deque([node for node in indegree if indegree[node] == 0])
        recipes = set(recipes)
        res = []
        while q:
            curr = q.popleft()
            if curr in recipes:
                res.append(curr)
            for recipe in graph[curr]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    q.append(recipe)

        return res


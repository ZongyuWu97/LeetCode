class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        menu = list(zip(recipes, ingredients))
        graph = defaultdict(list)
        indegrees = {r: 0 for r in recipes}
        for r, ing in menu:
            for i in ing:
                graph[i].append(r) # parent is ing required to make child recipe 
                if i not in supplies:
                    indegrees[r] += 1 #if not present the child is dependent
        
        q = deque()
        possibleRecipe = []
        for r, v in indegrees.items():
            if v == 0:
                q.append(r)
                possibleRecipe.append(r)
        
        while q:
            currRecipe = q.popleft()
            for neiRecipe in graph[currRecipe]:
                indegrees[neiRecipe] -= 1
                if indegrees[neiRecipe] == 0:
                    possibleRecipe.append(neiRecipe) # the parent was possible to made so now the child can be made too
                    q.append(neiRecipe)
        return(possibleRecipe)
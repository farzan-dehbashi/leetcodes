class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ready, needed, graph = set(supplies), collections.defaultdict(int), collections.defaultdict(list)

        for recepie, ingredient_list in zip(recipes, ingredients):
            for ingredient in ingredient_list:
                if not ingredient in ready:
                    needed[recepie] += 1
                    graph[ingredient].append(recepie)

        q = deque([recepie for recepie in recipes if needed[recepie] == 0])
        res = []

        while q:
            recepie = q.popleft()
            res.append(recepie)

            for dependent in graph[recepie]:
                needed[dependent] -= 1
                if needed[dependent] == 0:
                    q.append(dependent)
        return res 
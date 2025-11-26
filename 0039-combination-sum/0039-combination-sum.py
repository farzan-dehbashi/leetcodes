class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, reamining):
            if reamining == 0:
                res.append(path[:])
                return
            
            if reamining < 0:
                return

            for i in range(start, len(candidates)):
                if candidates[i] > reamining:
                    break
                
                path.append(candidates[i])
                backtrack(i, path, reamining - candidates[i])
                path.pop()
        backtrack(0, [], target)
        return res
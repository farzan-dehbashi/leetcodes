class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2:
            return []

        count, res = collections.Counter(changed), []
        for num in sorted(count):
            if count[num] > count[num*2]:
                return []
            
            if num == 0:
                if count[0] %2:
                    return []
                res += [0]* (int(count[0] / 2))
            else:
                res += [num] * count[num]
                count[num*2] -= count[num]
        return res
        

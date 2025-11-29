class TimeMap:

    def __init__(self):
        self.memo = collections.defaultdict(list)    

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memo[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if not key in self.memo:
            return ''
        
        vals = self.memo[key]
        l, r = 0, len(vals) - 1
        res = ''
        while l<=r:
            m = (l+r) // 2
            if vals[m][0] <= timestamp:
                res = vals[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
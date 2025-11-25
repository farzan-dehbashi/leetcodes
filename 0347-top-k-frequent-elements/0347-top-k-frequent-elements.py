class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = collections.Counter(nums)
        items = [(-freq, num) for num, freq in freqs.items()]
        heapq.heapify(items)
        res = []
        for _ in range(k):
            _, element = heapq.heappop(items)
            res.append(element)
        return res
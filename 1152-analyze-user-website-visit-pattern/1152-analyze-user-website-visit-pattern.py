class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        visits = collections.defaultdict(list)
        for i, user in enumerate(username):
            visits[user].append((timestamp[i], website[i]))
        for user in visits:
            visits[user].sort()
        
        patterns = {}

        for user in visits:
            if len(visits[user]) < 3:
                continue
            websites = [site for _, site in visits[user]]
            seen = set(combinations(websites, 3))
            for pattern in seen:
                patterns[tuple(pattern)] = patterns.get(tuple(pattern), 0) + 1
        
        freqs = [(-freq, pattern) for (pattern, freq) in patterns.items()]
        heapq.heapify(freqs)
        _, pattern = heapq.heappop(freqs)
        return pattern
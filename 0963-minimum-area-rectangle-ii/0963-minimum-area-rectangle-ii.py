class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        point_dict = {tuple(p): i for i, p in enumerate(points)}
        min_area = float('inf')

        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i == j:
                    continue
                for k, p3 in enumerate(points):
                    if k in [i, j]:
                        continue
                    
                    expected_p4 = (p2[0] + p3[0] - p1[0], p2[1] + p3[1] - p1[1])

                    if not expected_p4 in point_dict:
                        continue
                    
                    dx1, dy1 = p2[0] - p1[0], p2[1] - p1[1]
                    dx2, dy2 = p3[0] - p1[0], p3[1] - p1[1]

                    if dx1*dx2 + dy2*dy1 != 0:
                        continue
                    
                    area = (dx1**2 + dy1**2) ** 0.5 * (dx2**2 + dy2**2)**0.5
                    min_area = min(min_area, area)
        return 0 if min_area == float('inf') else min_area
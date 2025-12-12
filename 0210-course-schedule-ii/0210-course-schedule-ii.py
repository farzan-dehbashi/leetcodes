class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree, res, dep = collections.defaultdict(int), [], collections.defaultdict(set)
        for course, pre in prerequisites:
            dep[pre].add(course)
            indegree[course] += 1
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        while queue:
            course = queue.popleft()
            res.append(course)

            for next_course in dep[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)
        return res if len(res) == numCourses else []
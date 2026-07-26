class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        indexed_tasks = [(task[0], task[1], i) for i, task in enumerate(tasks)]
        indexed_tasks.sort(key=lambda x: x[0])
        result = []
        min_heap = []
        curr_time = 0
        task_idx = 0
        n = len(tasks)
        
        while task_idx < n or min_heap:
            if not min_heap and curr_time < indexed_tasks[task_idx][0]:
                curr_time = indexed_tasks[task_idx][0]
            while task_idx < n and indexed_tasks[task_idx][0] <= curr_time:
                enqueue_time, proc_time, orig_idx = indexed_tasks[task_idx]
                heapq.heappush(min_heap, (proc_time, orig_idx))
                task_idx += 1
            proc_time, orig_idx = heapq.heappop(min_heap)
            curr_time += proc_time
            result.append(orig_idx)
        return result
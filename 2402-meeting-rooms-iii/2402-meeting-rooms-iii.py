import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        empty_rooms, full_rooms, usage = list(range(n)), [], defaultdict(int)
        heapq.heapify(empty_rooms)

        for s, e in meetings:
            while full_rooms and full_rooms[0][0] <= s:
                _, room = heapq.heappop(full_rooms)
                heapq.heappush(empty_rooms, room)
            
            if empty_rooms:
                room = heapq.heappop(empty_rooms)
                usage[room] += 1
                heapq.heappush(full_rooms,  (e, room))
            else:
                earliest_end, room =heapq.heappop(full_rooms)
                usage[room] += 1
                wait_time = earliest_end - s
                heapq.heappush(full_rooms, (wait_time+e, room))
        
        max_used = max_room = -1
        for room in range(n):
            if usage[room] > max_used:
                max_used = usage[room]
                max_room = room
        return max_room

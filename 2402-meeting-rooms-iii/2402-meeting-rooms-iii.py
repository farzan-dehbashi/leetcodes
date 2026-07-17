import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        free_rooms = list(range(n))
        heapq.heapify(free_rooms)
        busy_rooms = []
        room_usage = defaultdict(int)
        for start, end in meetings:
            while busy_rooms and busy_rooms[0][0] <= start:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room)
            
            if free_rooms:
                room = heapq.heappop(free_rooms)
                room_usage[room] += 1
                heapq.heappush(busy_rooms, (end, room))

            else:
                earliest_end, room = heapq.heappop(busy_rooms)
                room_usage[room] += 1
                wait = earliest_end - start
                heapq.heappush(busy_rooms, (end+wait, room))
        
        max_used = max_room = -1
        for room in range(n):
            if room_usage[room] > max_used:
                max_used = room_usage[room]
                max_room = room
        return max_room

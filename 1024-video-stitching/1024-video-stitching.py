class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(key= lambda x: (x[0], -x[1]))

        c = cur_end = farthest = i = 0

        while cur_end < time:
            while i < len(clips) and clips[i][0] <= cur_end:
                farthest = max(farthest, clips[i][1])
                i += 1
            
            if farthest == cur_end:
                return -1
            
            cur_end = farthest
            c+=1
        return c
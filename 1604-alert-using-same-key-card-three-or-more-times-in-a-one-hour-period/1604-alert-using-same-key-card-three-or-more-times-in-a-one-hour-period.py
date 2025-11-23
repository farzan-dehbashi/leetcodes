class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        def toMins(hourMin):
            hour = int(hourMin[:2])
            minute = int(hourMin[3:])
            return minute + hour * 60
        names = collections.defaultdict(list)
        userList = []
        for i, name in enumerate(keyName):
            names[name].append(toMins(keyTime[i]))
        
        for name, times in names.items():
            if len(times) < 3:
                continue
            
            times.sort()
            l, r = 0, 2
            while r < len(times):
                if times[r] - times[l] <= 60:
                    userList.append(name)
                    break
                r, l = r+1, l+1
        userList.sort()
        return userList
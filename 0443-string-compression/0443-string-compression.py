class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) == 0:
            return 0
        chars.append('*')
        pre, count, res = chars[0], 1, []
        for i, char in enumerate(chars[1:]):
            if char == pre:
                count += 1
            else:
                if count == 1:
                    res.append(pre)
                else:
                    res = res + [pre] + list(str(count))
                pre, count = char, 1
        chars[:] = res
        return len(res)

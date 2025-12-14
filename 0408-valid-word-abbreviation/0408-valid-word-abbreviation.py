class Solution:
    def validWordAbbreviation(self, word: str, pattern: str) -> bool:
        wc = pc = 0
        while wc < len(word) and pc < len(pattern):
            if pattern[pc].isnumeric():
                if pattern[pc] == '0':
                    return False
                num = 0
                while pc < len(pattern) and pattern[pc].isnumeric():
                    num = num * 10 + int(pattern[pc])
                    pc += 1
                wc += num
            else:
                # alphabetic
                if not wc < len(word) or not pc < len(pattern) or not pattern[pc] == word[wc]:
                    return False
                pc, wc = pc+1, wc+1
        return pc == len(pattern) and wc == len(word)
            
class Solution:

    def encode(self, strs: List[str]) -> str:
        en_st = ""
        for st in strs:
            en_st += str(len(st)) + "#"
            en_st += st
        print("en_st - ",en_st)
        return en_st

    def decode(self, s: str) -> List[str]:
        de_st_lst = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            if j >= len(s):
                break
            
            length = int(s[i:j])
            start = j + 1
            end = start + length
            de_st_lst.append(s[start : end])
            i = end
        return de_st_lst

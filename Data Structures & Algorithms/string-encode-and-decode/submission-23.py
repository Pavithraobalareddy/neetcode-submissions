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
        while i < len(s): #run through the len of the string
            j = i #assign j to index of last end
            while j < len(s) and s[j] != "#": 
                j += 1 #increment j until the delimiter is found
            if j >= len(s): #check for the end of the whole string
                break
            
            length = int(s[i:j]) # extract the length of the string
            start = j + 1 #j is pointing to delimiter, so start of string is j+1
            end = start + length #end is point to the length of the next string
            de_st_lst.append(s[start : end]) #slice the string. Note: string is extracted end-1 index
            i = end # assign the i to the end i.e length of next string
        return de_st_lst

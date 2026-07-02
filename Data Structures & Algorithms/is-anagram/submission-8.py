from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        arr = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            arr[index] += 1
        
        for char in t:
            index = ord(char) - ord('a')
            arr[index] -= 1

        for i in range(26):
            if arr[i] != 0:
                return False
        return True
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        for word in strs: #iterate through the list
            string = ''.join(sorted(word)) #sort the each string in list
            if string in my_dict: #if the string in dictionary then append word
                my_dict[string].append(word)
            else: #if the string is not in dictionary then just add word
                my_dict[string] = [word]
        return list(my_dict.values()) #return the values in dictory
            
            
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        for i in nums:
            if i not in my_dict:
                my_dict[i] = True
            else :
                return True
        return False

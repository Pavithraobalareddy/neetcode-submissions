class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        product = 1
        lst = []
        for i in range(len(nums)-1):
            start = i + 1
            end = (len(nums) - i) - 1
            while start < len(nums):
                product *= nums[start]
                start += 1
            prefix[i] = product
            product = 1
            #print("prefix", prefix)

            while end > 0:
                product *= nums[end - 1]
                end -= 1
            suffix[(len(nums)-i)-1] = product
            product = 1
            #print("suffix", suffix)
        for j in range(len(nums)):
            lst.append(prefix[j] * suffix[j])
        return lst
            

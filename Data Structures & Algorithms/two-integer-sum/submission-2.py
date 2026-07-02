class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = []
        if len(nums) <= 2 and len(nums) >= 1000:
            return list

        for i in range(len(nums)):
            diff = target - nums[i]
            #print("diff",diff)
            for j in range(len(nums)):
                if nums[j] == diff and i !=j:
                    #print("append",j)
                    list.append(i)
                    list.append(j)
                    #print("orginal",list)
                    return list
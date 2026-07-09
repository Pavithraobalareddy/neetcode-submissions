from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = Counter()
        for num in sorted(nums):
            my_dict[num] += 1
        #print("my_dict", my_dict)
        top_counts = my_dict.most_common(k)
        #print("top_counts", top_counts)
        k_counts = [item[0] for item in top_counts]
        #print("k_counts", k_counts)
        return k_counts

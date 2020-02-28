class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {} 
        for i, n in enumerate(nums):
            complement = target - n
            if complement in hash_table:
                return [hash_table[complement], i]
            else:
                hash_table[n] = i
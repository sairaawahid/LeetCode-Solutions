class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # nums.sort()       
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i -1]:
        #             return True
        # return False

        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
       
       # check both monotonic increasing and decreasing
        increase, decrease = True, True

        for i in range(len(nums) - 1):
            if not (nums[i] <= nums[i + 1]):
                increase = False
            if not (nums[i] >= nums[i + 1]):
                decrease = False

        return increase or decrease

        '''
        check monotovic increasing only

        if nums[-1] - nums[0] < 0:
            nums.reverse()
        for i range(len(nums) - 1):
            if not (nums[i] <= nums[i + 1]):
                return False
        return True
        
        '''
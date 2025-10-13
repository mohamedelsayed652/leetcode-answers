class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        low = 0
        high = len(nums) - 1
        while low <= high:
            i = (low + high) // 2
            if target == nums[i]:
                return i
            elif target > nums[i]:
                low = i + 1
            else:
                high = i - 1
        return low

        
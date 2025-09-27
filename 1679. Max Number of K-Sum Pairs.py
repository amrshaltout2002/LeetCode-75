class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = 0
        while len(nums) > 1:
            if nums[0] + nums[-1] == k:
                n += 1
                nums.pop(0)
                nums.pop()
            elif nums[0] + nums[-1] > k:
                nums.pop()
            else:
                nums.pop(0)
        return n
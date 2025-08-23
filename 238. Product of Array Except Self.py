class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lst = [1] * len(nums)

        left = 1
        for i in range(len(nums)):
            lst[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums)-1, -1, -1):
            lst[i] *= right
            right *= nums[i]

        return lst
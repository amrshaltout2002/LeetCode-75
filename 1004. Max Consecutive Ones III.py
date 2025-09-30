class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, maxx, num_zeros = 0, 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1
            maxx = max(maxx, (r-l+1))
        return maxx
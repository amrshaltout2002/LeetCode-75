class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxAvg = -9999999
        sumLst = -1
        left = 0
        right = k
        if len(nums) <= k:
            print(f"sum: {sum(nums)}, len: {len(nums)}")
            maxAvg = sum(nums) / len(nums)
        else:
            sumLst = sum(nums[0:k])
            for i in range(len(nums)):
                avgLst = sumLst/k
                maxAvg = max(avgLst, maxAvg)
                if right >= len(nums):
                    break

                sumLst = sumLst - nums[left]
                sumLst = sumLst + nums[right]
                left += 1
                right +=1        
                
        return maxAvg
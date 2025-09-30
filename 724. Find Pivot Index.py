class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        i = 0
        summ1, summ2 = 0, 0
        lst1 = []
        lst2 = []
        output = -1
        for i in range(len(nums)):
            k = (len(nums)-1) - i

            summ1 += nums[i]
            lst1.append(summ1)

            summ2 += nums[k]
            lst2.append(summ2)
        lst2 = lst2[::-1]

        for i in range(len(nums)):
            if lst1[i] == lst2[i]:
                output = i
                break
        return output
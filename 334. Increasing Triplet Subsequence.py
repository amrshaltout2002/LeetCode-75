class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        lst = []
        lst.append(nums[0])
        counter = 0
        for i in nums:
            if i <= lst[0]:
                lst[0] = i
            else:
                if i > lst[-1]:
                    lst.append(i)
                    counter += 1
                else:
                    lst.pop()
                    lst.append(i)

            if counter == 2:
                return True
        return False
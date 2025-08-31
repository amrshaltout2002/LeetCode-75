class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lst = []
        counter = 0

        for i in nums:
            if i != 0:
                lst.append(i)
            else:
                counter += 1

        for i in range(counter):
            lst.append(0)

        nums[:] = lst
        return nums
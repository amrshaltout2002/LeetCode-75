class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        lst = []
        x = list((nums1^nums2)&nums1)
        y = list((nums1^nums2)&nums2)
        lst.append(x)
        lst.append(y)
        return lst
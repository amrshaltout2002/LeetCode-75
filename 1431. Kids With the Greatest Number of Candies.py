class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        result = []
        for i in candies:
            if i + extraCandies >= max_num:
                result.append(True)
            else:
                result.append(False)
        return result


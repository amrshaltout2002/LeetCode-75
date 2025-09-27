class Solution:
    def maxArea(self, height: List[int]) -> int:
        perimeter = -1
        n = len(height) - 1

        if len(height) == 1:
            perimeter = 0
        else:
            while len(height) > 1:
                if height[0] < height[-1]:
                    perimeter = max(height[0] * n, perimeter)
                    n -= 1
                    height.pop(0)
                else:
                    perimeter = max(height[-1] * n, perimeter)
                    n -= 1
                    height.pop()

        return perimeter

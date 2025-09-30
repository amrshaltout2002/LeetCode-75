class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxx, summ = 0, 0

        for i in gain:
            summ += i
            maxx = max(summ, maxx)
        return maxx
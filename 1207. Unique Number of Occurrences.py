class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dec = {}

        for i in arr:
            if i not in dec.keys():
                dec[i] = 1
            else:
                dec[i] += 1

        st = set(dec.values())
        if len(st) == len(dec.keys()):
            return True
        else:
            return False
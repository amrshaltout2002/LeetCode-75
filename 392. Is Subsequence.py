class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0

        if s == "":
            return True

        for i in range(len(t)):
            if j < len(s) and s[j] == t[i]:
                j += 1

        if j < len(s) or j == 0:
            return False

        return True
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        right = k
        lst = s[0:k]
        n = len(s)
        maxVowels = lst.count("a") + lst.count("i") + lst.count("e") + lst.count("u") + lst.count("o")
        currentVowels = maxVowels
        while right < n:
            if lst[0] in "aieuo":
                currentVowels -= 1
            if s[right] in "aieuo":
                currentVowels += 1
            lst = lst[1:] + s[right]
            maxVowels = max(x, y)
            left += 1
            right += 1
        return x
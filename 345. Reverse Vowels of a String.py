class Solution:
    def reverseVowels(self, s: str) -> str:
        lst = []
        s = list(s)
        for i in range(len(s)):
            if s[i] in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
                 lst.append(s[i])
                 s[i] = 0

        for i in range(len(s)):
            if s[i] == 0:
                s[i] = lst[-1]
                lst.pop()

        return "".join(s)
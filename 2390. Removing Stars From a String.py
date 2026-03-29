class Solution:
    def removeStars(self, s: str) -> str:
        text = []
        for i in range(len(s)):
            if s[i] != '*':
                text.append(s[i])
            else:
                text.pop(len(text)-1)
        
        return ''.join(text)
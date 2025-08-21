class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
      max_len = max(len(word1), len(word2))
      word = ""
      if len(word1) < max_len:
          word1 = word1 + " " * (max_len - len(word1))

      if len(word2) < max_len:
          word2 = word2 + " " * (max_len - len(word2))

      for i in range(0, max_len):
          if word1[i] == " ":
              word = word + word2[i]
          elif word2[i] == " ":
              word = word + word1[i]
          else:
              word = word + word1[i] + word2[i]

      return word

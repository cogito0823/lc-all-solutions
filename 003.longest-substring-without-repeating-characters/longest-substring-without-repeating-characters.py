class Solution(object):
  def _lengthOfLongestSubstring(self, s):
    """
    :type s: str
    :rtype: int
    """
    d = collections.defaultdict(int)
    l = ans = 0
    for i, c in enumerate(s):
      while l > 0 and d[c] > 0:
        d[s[i - l]] -= 1
        l -= 1
      d[c] += 1
      l += 1
      ans = max(ans, l)
    return ans

  def lengthOfLongestSubstring(self, s):
    d = {}
    start = 0
    ans = 0
    for i, c in enumerate(s):
      if c in d:
        start = max(start, d[c] + 1)
      d[c] = i
      ans = max(ans, i - start + 1)
    return ans

  
#########################     方法二      ################################
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s1 = ''
        lens = 0
        for char in list(s):
            s1 = s1.split(char)[-1] + char
            lens = len(s1) if len(s1) > lens else lens
        return lens


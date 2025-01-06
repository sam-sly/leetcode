import math

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = s[0]
        pivot = 0.5
        range = 0.5

        while pivot <= len(s) - len(longest) / 2.0:
            range = math.ceil(len(longest) / 2.0)
            start = int(math.ceil(pivot - range))
            end = int(math.floor(pivot + range))

            i = start
            j = end

            while i < j and i >= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i += 1
                j -= 1

            if i >= j:
                i = start - 1
                j = end + 1

                while i >= 0 and j < len(s):
                    if s[i] != s[j]:
                        break
                    i -= 1
                    j += 1
                
                longest = s[i+1:j]
            
            pivot += 0.5

        return longest
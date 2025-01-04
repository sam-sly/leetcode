class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        longest = 0
        dict = {}

        for i in range(len(s)):
            if s[i] in dict:
                if dict[s[i]] < start:
                    dict.pop(s[i])
                else:
                    length = i - start
                    if length > longest:
                        longest = length
                    
                    start = dict[s[i]] + 1

            dict[s[i]] = i
        
        length = len(s) - start
        if length > longest:
            longest = length

        return longest
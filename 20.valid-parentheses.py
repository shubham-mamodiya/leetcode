#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s_length = len(s)
        if s_length % 2 != 0:
            return False
        
        iterations = s_length / 2

        for i in range(iterations):
            if s[i] != s[-1 * i]:
                return False
        return True

# @lc code=end


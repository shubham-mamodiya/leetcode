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

        symbols = {'(': ')', '[': ']', '{': '}'}
        keys = symbols.keys()
        values = symbols.values()

        ending_of_openings = ''
        endings_in_string = ''

        for char in s:
            if char in values:
                endings_in_string += char
            elif char in keys:
                ending_of_openings += symbols[char]
            else:
                return False
        
        if endings_in_string != ending_of_openings:
            return False

        return True 

# @lc code=en
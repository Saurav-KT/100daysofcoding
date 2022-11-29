# A pangram is a sentence where every letter of the English alphabet appears at least once.
# Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.
# Example 2:
#
# Input: sentence = "leetcode"
# Output: false

import string
class Solution:

    def checkIfPangram(self, sentence: str) -> bool:
        counter = 0
        if 1 <= len(sentence) <= 1000:
            for element in string.ascii_lowercase:
                if element not in sentence:
                    counter += 1
            if counter == 0:
                return True
            else:
                return False


obj = Solution()
obj.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
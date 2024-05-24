class Solution:
    def isPalindrome(self, x: int) -> bool:
        numbers = [i for i in str(x)]
        new = numbers[::-1]
        if new == numbers:
            return True
        else:
            return False

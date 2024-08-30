# LeetCode for TikTok 9
# by F.C. Vogel
# Palindrome Number (reminders)
# https://leetcode.com/problems/two-sum/description/

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0: return False
    
    x_temp = x
    revers = 0
    
    while x > 0:
        revers = revers*10 + x%10
        x //= 10
        
    return revers == x_temp
    
if __name__ == '__main__':
    
    x = 1221

    print(isPalindrome(x))
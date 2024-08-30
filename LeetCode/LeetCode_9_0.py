# LeetCode for TikTok 9
# by F.C. Vogel
# Palindrome Number (brut force)
# https://leetcode.com/problems/two-sum/description/

def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0: return False
    x_t = str(x)
    x_l = list(x_t)
    L = len(x_l)//2
    for i in range(L):
        if x_l[i] != x_l[-(i+1)]:
            return False
            break
        else:
            pass
    return True

if __name__ == '__main__':
    x = 121
    print(isPalindrome(x))

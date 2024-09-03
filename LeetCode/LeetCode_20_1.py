# LeetCode for TikTok 20
# by F.C. Vogel
# Valid Parentheses (optimized)
# https://leetcode.com/problems/valid-parentheses/description/

def isValid(s):
    
    code = {')':'(',']':'[','}':'{'}
    stack = []
    
    top = ''
    for char in s:
        if char in code:
            if stack:
                top = stack.pop()
            else:
                top = ''
            if code[char] != top: return False
        else:
            stack.append(char)
            
    return not stack

if __name__ == '__main__':
    
    s = "()))"
    print(isValid(s))
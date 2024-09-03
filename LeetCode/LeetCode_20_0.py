# LeetCode for TikTok 20
# by F.C. Vogel
# Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

def isValid(s):    
    code = {'(':1,')':-1,'[':2,']':-2,'{':3,'}':-3}
    stack = []
    
    Valid = True
    
    for i in range(len(s)):
        if len(stack) == 0 and code[s[i]] < 0:
            Valid = False
            break 
        elif code[s[i]]>0:
            stack.append(code[s[i]])
        else:
            if stack[-1]+code[s[i]] != 0:
                Valid = False
                break
            else:
                stack.pop(-1)
    if len(stack) != 0:
        Valid = False 
    return Valid

if __name__ == '__main__':
    
    s = "({)"
    print(isValid(s))
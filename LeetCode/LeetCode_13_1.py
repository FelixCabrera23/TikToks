# LeetCode for TikTok 13
# by F.C. Vogel
# Roman to Integer (brute force is faster)
# https://leetcode.com/problems/roman-to-integer/description/

def romanToInt(s):
    romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    num = 0
    for i in range(len(s)):
        if i+1<len(s) and romans[s[i]] < romans[s[i+1]]:
            num -= romans[s[i]]
        else:
            num += romans[s[i]]
    return num
    
if __name__ == '__main__':
    s = 'MCMXCIV'
    
    print(romanToInt(s))
        
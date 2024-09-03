# LeetCode for TikTok 13
# by F.C. Vogel
# Roman to Integer
# https://leetcode.com/problems/roman-to-integer/description/

def romanToInt(s):
    romans = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    
    num = 0
    prev = 0
    for char in reversed(s):
        temp = romans[char]
        if temp >= prev:
            num+=temp
        else:
            num-=temp
        prev = temp
    return num 
    
if __name__ == '__main__':
    s = 'MCMXCIV'
    
    print(romanToInt(s))
        
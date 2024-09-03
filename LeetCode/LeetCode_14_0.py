# LeetCode for TikTok 14
# by F.C. Vogel
# Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/description/

def longestCommonPrefix(strs):
    common = True
    last = strs.pop()
    output = ''
    for i in range(len(last)):
        char = last[i]
        for word in strs:
            if i >= len(word):
                common = False
                break
            elif char != word[i]:
                common = False
            else:
                pass
        if common: output+=char
    return output

if __name__ == '__main__':
    strs = ["","b"]
    print(longestCommonPrefix(strs))
            


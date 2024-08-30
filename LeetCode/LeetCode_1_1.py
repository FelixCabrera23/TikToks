# LeetCode for TikTok 1
# by F.C. Vogel
# Two Sum (brute force 2)
# https://leetcode.com/problems/two-sum/description/

def twoSum(nums,target):
    """
    Takes nums (list) and cheks for two
    elements such that sumed are target (int)
    and returns this in a list
    """
    j = len(nums)-1
    while len(nums)>0:
        fix = nums.pop()
        i = 0
        for num in nums:
            if fix + num == target:
                return i,j
                break
            i += 1
        j-=1

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
        
    print(twoSum(nums,target))
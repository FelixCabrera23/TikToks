# LeetCode for TikTok 1
# by F.C. Vogel
# Two Sum (hash map)
# https://leetcode.com/problems/two-sum/description/

def twoSum(nums,target):
    """
    Takes nums (list) and cheks for two
    elements such that sumed are target (int)
    and returns this in a list
    """
    hash_map = {}
    for i in range(len(nums)):
        difference = target - nums[i]
        if difference in hash_map:
            return [i,hash_map[difference]]
        hash_map[nums[i]] = i

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
        
    print(twoSum(nums,target))
    
        